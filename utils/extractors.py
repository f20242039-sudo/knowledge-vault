"""
utils/extractors.py
Extracts plain text from uploaded files (PDF, DOCX, TXT).
No API calls — pure local processing.
"""

import io
import logging

logger = logging.getLogger(__name__)


def extract_pdf(file_bytes: bytes) -> str:
    """Extract text from a PDF file using PyMuPDF."""
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        logger.warning(f"PDF extraction failed: {e}")
        return ""


def extract_docx(file_bytes: bytes) -> str:
    """Extract text from a Word document using python-docx."""
    try:
        from docx import Document
        doc = Document(io.BytesIO(file_bytes))
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n".join(paragraphs).strip()
    except Exception as e:
        logger.warning(f"DOCX extraction failed: {e}")
        return ""


def extract_txt(file_bytes: bytes) -> str:
    """Decode a plain text file."""
    try:
        return file_bytes.decode("utf-8").strip()
    except UnicodeDecodeError:
        try:
            return file_bytes.decode("latin-1").strip()
        except Exception as e:
            logger.warning(f"TXT extraction failed: {e}")
            return ""


def extract(file_bytes: bytes, filename: str) -> str:
    """
    Router: picks the right extractor based on file extension.
    Returns extracted plain text, or empty string on failure.
    """
    name = filename.lower()

    if name.endswith(".pdf"):
        text = extract_pdf(file_bytes)
    elif name.endswith(".docx"):
        text = extract_docx(file_bytes)
    elif name.endswith(".txt") or name.endswith(".md"):
        text = extract_txt(file_bytes)
    else:
        logger.warning(f"Unsupported file type: {filename}")
        return ""

    if not text:
        logger.warning(f"No text extracted from: {filename}")

    return text
