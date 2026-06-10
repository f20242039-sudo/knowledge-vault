"""
tests/test_tagger.py
Tests for Pydantic schemas and Groq tagger (API is mocked — no real calls made).
Run with: pytest tests/test_tagger.py -v
"""

import pytest
from unittest.mock import MagicMock, patch
from ai.schemas import DocumentTagSchema, SkillTag
from ai.groq_tagger import tag_document


# ── Schema tests (no mocking needed) ──────────────────────────────────────────

def test_valid_schema_parses():
    data = {
        "description": "A document about neural networks.",
        "difficulty": "Intermediate",
        "subjects": ["Machine Learning"],
        "skills": [
            {"name": "Backpropagation", "coverage": 90},
            {"name": "Gradient descent", "coverage": 70},
        ],
    }
    schema = DocumentTagSchema(**data)
    assert schema.difficulty == "Intermediate"
    assert len(schema.skills) == 2
    assert schema.skills[0].coverage == 90


def test_invalid_difficulty_rejected():
    with pytest.raises(Exception):
        DocumentTagSchema(
            description="Test",
            difficulty="Expert",   # not a valid value
            subjects=["Math"],
            skills=[],
        )


def test_coverage_out_of_range_rejected():
    with pytest.raises(Exception):
        SkillTag(name="NumPy", coverage=150)


def test_coverage_zero_allowed():
    tag = SkillTag(name="Calculus", coverage=0)
    assert tag.coverage == 0


# ── Tagger tests (Groq API mocked) ────────────────────────────────────────────

MOCK_GROQ_RESPONSE = """{
  "description": "An introduction to linear algebra covering vectors and matrices.",
  "difficulty": "Beginner",
  "subjects": ["Mathematics"],
  "skills": [
    {"name": "Matrix operations", "coverage": 80},
    {"name": "Eigenvalues", "coverage": 50}
  ]
}"""


def make_mock_groq(content: str):
    """Build a mock that mimics groq.Client.chat.completions.create()"""
    mock_message = MagicMock()
    mock_message.content = content
    mock_choice = MagicMock()
    mock_choice.message = mock_message
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = mock_response
    return mock_client


@patch("ai.groq_tagger.Groq")
def test_tag_document_returns_schema(mock_groq_class):
    mock_groq_class.return_value = make_mock_groq(MOCK_GROQ_RESPONSE)
    result = tag_document("Some document text about linear algebra.")
    assert isinstance(result, DocumentTagSchema)
    assert result.difficulty == "Beginner"
    assert result.subjects == ["Mathematics"]
    assert result.skills[0].name == "Matrix operations"


@patch("ai.groq_tagger.Groq")
def test_tag_document_strips_markdown_fences(mock_groq_class):
    wrapped = f"```json\n{MOCK_GROQ_RESPONSE}\n```"
    mock_groq_class.return_value = make_mock_groq(wrapped)
    result = tag_document("Some text.")
    assert isinstance(result, DocumentTagSchema)


@patch("ai.groq_tagger.Groq")
def test_tag_document_raises_after_retries(mock_groq_class):
    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = Exception("API down")
    mock_groq_class.return_value = mock_client
    with pytest.raises(ValueError, match="failed after"):
        tag_document("Some text.", retries=1)
