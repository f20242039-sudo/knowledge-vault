"""
tests/test_ingest.py
Integration tests for the full pipeline — all external calls mocked.
Run with: pytest tests/test_ingest.py -v
"""

import pytest
from unittest.mock import patch, MagicMock
from pipeline.ingest import ingest_document, IngestResult
from ai.schemas import DocumentTagSchema, SkillTag

SAMPLE_SCHEMA = DocumentTagSchema(
    description="An introduction to neural networks and backpropagation.",
    difficulty="Intermediate",
    subjects=["Machine Learning", "Mathematics"],
    skills=[
        SkillTag(name="Backpropagation", coverage=90),
        SkillTag(name="Gradient descent", coverage=70),
    ],
)

SAMPLE_TEXT = "This document covers neural networks and gradient descent in detail."


@patch("pipeline.ingest.db.insert_tags")
@patch("pipeline.ingest.db.insert_document", return_value="mock-uuid-5678")
@patch("pipeline.ingest.embed", return_value=[0.1] * 384)
@patch("pipeline.ingest.tag_document", return_value=SAMPLE_SCHEMA)
@patch("pipeline.ingest.extract", return_value=SAMPLE_TEXT)
def test_ingest_returns_result(mock_extract, mock_tag, mock_embed, mock_insert_doc, mock_insert_tags):
    result = ingest_document(b"fake pdf bytes", "notes.pdf")
    assert isinstance(result, IngestResult)
    assert result.document_id == "mock-uuid-5678"
    assert result.filename == "notes.pdf"
    assert result.difficulty == "Intermediate"
    assert "Machine Learning" in result.subjects
    assert len(result.skills) == 2


@patch("pipeline.ingest.db.insert_tags")
@patch("pipeline.ingest.db.insert_document", return_value="mock-uuid-5678")
@patch("pipeline.ingest.embed", return_value=[0.1] * 384)
@patch("pipeline.ingest.tag_document", return_value=SAMPLE_SCHEMA)
@patch("pipeline.ingest.extract", return_value=SAMPLE_TEXT)
def test_ingest_calls_all_steps(mock_extract, mock_tag, mock_embed, mock_insert_doc, mock_insert_tags):
    ingest_document(b"fake pdf bytes", "notes.pdf")
    mock_extract.assert_called_once()
    mock_tag.assert_called_once_with(SAMPLE_TEXT)
    mock_embed.assert_called_once_with(SAMPLE_TEXT)
    mock_insert_doc.assert_called_once()
    mock_insert_tags.assert_called_once()


@patch("pipeline.ingest.extract", return_value="")
def test_ingest_raises_on_empty_text(mock_extract):
    with pytest.raises(ValueError, match="Could not extract"):
        ingest_document(b"empty", "blank.pdf")


@patch("pipeline.ingest.db.insert_tags")
@patch("pipeline.ingest.db.insert_document", return_value="mock-uuid-5678")
@patch("pipeline.ingest.embed", return_value=[0.1] * 384)
@patch("pipeline.ingest.tag_document", side_effect=ValueError("Groq failed"))
@patch("pipeline.ingest.extract", return_value=SAMPLE_TEXT)
def test_ingest_raises_on_tagging_failure(mock_extract, mock_tag, mock_embed, mock_insert_doc, mock_insert_tags):
    with pytest.raises(ValueError, match="Groq failed"):
        ingest_document(b"bytes", "notes.pdf")
