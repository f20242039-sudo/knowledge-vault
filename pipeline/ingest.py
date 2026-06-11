"""
pipeline/ingest.py
Orchestrates the full document ingestion pipeline:
  1. Extract text from uploaded file
  2. Tag with AI (Groq or Ollama — configured via provider_cfg)
  3. Embed text into a 384-dim vector
  4. Store document + tags in Supabase

This is the single function the Streamlit UI calls on upload.
"""

import logging
from dataclasses import dataclass

from utils.extractors import extract
from ai.tagger import tag_document
from ai.embedder import embed
from ai.schemas import DocumentTagSchema
from db import supabase_client as db

logger = logging.getLogger(__name__)


@dataclass
class IngestResult:
    """Returned to the UI after a successful ingest."""
    document_id: str
    filename: str
    description: str
    difficulty: str
    subjects: list[str]
    skills: list[dict]   # [{"name": str, "coverage": int}]


def ingest_document(
    file_bytes: bytes,
    filename: str,
    provider_cfg: dict | None = None,
) -> IngestResult:
    """
    Full pipeline: file bytes in, structured result out.

    Args:
        file_bytes:   Raw bytes of the uploaded file.
        filename:     Original filename (used to detect file type).
        provider_cfg: AI provider config passed from the UI sidebar.
                      Shape: {"provider": "groq"|"ollama", "api_key": ...,
                               "model": ..., "base_url": ...}
                      When None, falls back to GROQ_API_KEY env var.

    Returns:
        IngestResult with document ID and all generated tags.

    Raises:
        ValueError: If the file yields no text, or AI tagging fails.
    """

    # ── Step 1: Extract text ───────────────────────────────────────────────────
    logger.info(f"[1/4] Extracting text from: {filename}")
    text = extract(file_bytes, filename)
    if not text:
        raise ValueError(
            f"Could not extract any text from '{filename}'. "
            "The file may be empty, scanned, or an unsupported format."
        )

    # ── Step 2: AI tagging ────────────────────────────────────────────────────
    provider_label = (provider_cfg or {}).get("provider", "groq").upper()
    logger.info(f"[2/4] Tagging document with {provider_label}...")
    tags: DocumentTagSchema = tag_document(text, provider_cfg=provider_cfg)

    # ── Step 3: Embed ─────────────────────────────────────────────────────────
    logger.info(f"[3/4] Generating embedding...")
    vector = embed(text)

    # ── Step 4: Store ─────────────────────────────────────────────────────────
    logger.info(f"[4/4] Storing in Supabase...")
    doc_id = db.insert_document(
        filename=filename,
        raw_text=text,
        description=tags.description,
        difficulty=tags.difficulty,
        embedding=vector,
    )
    db.insert_tags(doc_id, tags)

    logger.info(f"Ingest complete for '{filename}' → {doc_id}")

    return IngestResult(
        document_id=doc_id,
        filename=filename,
        description=tags.description,
        difficulty=tags.difficulty,
        subjects=tags.subjects,
        skills=[{"name": s.name, "coverage": s.coverage} for s in tags.skills],
    )
