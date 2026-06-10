"""
db/supabase_client.py
All database read/write operations for the Knowledge Vault.
No SQL lives anywhere else in the project — only here.
"""

import logging
import os

from supabase import create_client, Client
from ai.schemas import DocumentTagSchema
from utils.secrets import get_secret
logger = logging.getLogger(__name__)


def _get_client() -> Client:
    url = get_secret("SUPABASE_URL")
    key = get_secret("SUPABASE_KEY")
    return create_client(url, key)


# ── Write operations ───────────────────────────────────────────────────────────

def insert_document(
    filename: str,
    raw_text: str,
    description: str,
    difficulty: str,
    embedding: list[float],
    file_path: str = None,
) -> str:
    """
    Insert a document into the documents table.
    Returns the new document's UUID.
    """
    client = _get_client()
    response = (
        client.table("documents")
        .insert({
            "filename": filename,
            "file_path": file_path,
            "raw_text": raw_text,
            "description": description,
            "difficulty": difficulty,
            "embedding": embedding,
        })
        .execute()
    )
    doc_id = response.data[0]["id"]
    logger.info(f"Inserted document: {filename} → {doc_id}")
    return doc_id


def insert_tags(document_id: str, tags: DocumentTagSchema) -> None:
    """
    Insert all subject and skill tags for a document.
    """
    client = _get_client()
    rows = []

    for subject in tags.subjects:
        rows.append({
            "document_id": document_id,
            "tag_type": "subject",
            "name": subject,
            "coverage": None,
        })

    for skill in tags.skills:
        rows.append({
            "document_id": document_id,
            "tag_type": "skill",
            "name": skill.name,
            "coverage": skill.coverage,
        })

    if rows:
        client.table("tags").insert(rows).execute()
        logger.info(f"Inserted {len(rows)} tags for document {document_id}")


# ── Read operations ────────────────────────────────────────────────────────────

def get_all_documents() -> list[dict]:
    """
    Return all documents with their tags.
    """
    client = _get_client()
    docs = client.table("documents").select("id, filename, description, difficulty, created_at").execute().data
    for doc in docs:
        doc["tags"] = _get_tags_for_document(client, doc["id"])
    return docs


def get_document_by_id(doc_id: str) -> dict:
    """
    Return a single document with full details and tags.
    """
    client = _get_client()
    response = (
        client.table("documents")
        .select("id, filename, description, difficulty, created_at, raw_text")
        .eq("id", doc_id)
        .single()
        .execute()
    )
    doc = response.data
    doc["tags"] = _get_tags_for_document(client, doc_id)
    return doc


def search_documents(query_vector: list[float], limit: int = 10) -> list[dict]:
    """
    Semantic search: find documents most similar to the query vector.
    Uses the match_documents SQL function defined in the migration.
    """
    client = _get_client()
    response = client.rpc(
        "match_documents",
        {"query_embedding": query_vector, "match_count": limit}
    ).execute()

    results = response.data
    for doc in results:
        doc["tags"] = _get_tags_for_document(client, doc["id"])
    return results


def get_documents_by_tag(tag_type: str, tag_name: str) -> list[dict]:
    """
    Return all documents that have a specific tag.
    e.g. get_documents_by_tag("subject", "Machine Learning")
    """
    client = _get_client()
    tag_rows = (
        client.table("tags")
        .select("document_id")
        .eq("tag_type", tag_type)
        .eq("name", tag_name)
        .execute()
        .data
    )
    doc_ids = [row["document_id"] for row in tag_rows]
    if not doc_ids:
        return []

    docs = (
        client.table("documents")
        .select("id, filename, description, difficulty, created_at")
        .in_("id", doc_ids)
        .execute()
        .data
    )
    for doc in docs:
        doc["tags"] = _get_tags_for_document(client, doc["id"])
    return docs


def get_all_tags() -> dict[str, list[str]]:
    """
    Return all unique subject and skill tag names.
    Used to populate the tag filter browser.
    Returns: {"subject": [...], "skill": [...]}
    """
    client = _get_client()
    rows = client.table("tags").select("tag_type, name").execute().data
    subjects = sorted(set(r["name"] for r in rows if r["tag_type"] == "subject"))
    skills = sorted(set(r["name"] for r in rows if r["tag_type"] == "skill"))
    return {"subject": subjects, "skill": skills}


# ── Delete operations ──────────────────────────────────────────────────────────

def delete_document(doc_id: str) -> None:
    """
    Delete a document and all its tags (cascade handled by DB).
    """
    client = _get_client()
    client.table("documents").delete().eq("id", doc_id).execute()
    logger.info(f"Deleted document: {doc_id}")


# ── Internal helpers ───────────────────────────────────────────────────────────

def _get_tags_for_document(client: Client, document_id: str) -> list[dict]:
    rows = (
        client.table("tags")
        .select("tag_type, name, coverage")
        .eq("document_id", document_id)
        .execute()
        .data
    )
    return rows
