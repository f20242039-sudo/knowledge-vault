"""
tests/test_db.py
Tests for the Supabase client — all DB calls are mocked, no real DB needed.
Run with: pytest tests/test_db.py -v
"""

import pytest
from unittest.mock import MagicMock, patch
from ai.schemas import DocumentTagSchema, SkillTag


# ── Helpers ────────────────────────────────────────────────────────────────────

def make_mock_client(insert_return=None, select_return=None, rpc_return=None, delete_return=None):
    """Build a mock Supabase client."""
    client = MagicMock()

    # insert chain: .table().insert().execute()
    client.table.return_value.insert.return_value.execute.return_value.data = (
        insert_return or [{"id": "test-uuid-1234"}]
    )

    # select chain: .table().select().execute()
    client.table.return_value.select.return_value.execute.return_value.data = (
        select_return or []
    )

    # eq chain: .table().select().eq().execute()
    client.table.return_value.select.return_value.eq.return_value.execute.return_value.data = []

    # single chain
    client.table.return_value.select.return_value.eq.return_value.single.return_value.execute.return_value.data = (
        select_return[0] if select_return else {"id": "test-uuid-1234", "filename": "test.pdf"}
    )

    # in_ chain
    client.table.return_value.select.return_value.in_.return_value.execute.return_value.data = (
        select_return or []
    )

    # delete chain
    client.table.return_value.delete.return_value.eq.return_value.execute.return_value.data = []

    # rpc chain
    client.rpc.return_value.execute.return_value.data = rpc_return or []

    return client


SAMPLE_TAGS = DocumentTagSchema(
    description="A document about machine learning.",
    difficulty="Intermediate",
    subjects=["Machine Learning", "Mathematics"],
    skills=[
        SkillTag(name="Gradient descent", coverage=80),
        SkillTag(name="Backpropagation", coverage=60),
    ],
)


# ── Tests ──────────────────────────────────────────────────────────────────────

@patch("db.supabase_client.create_client")
def test_insert_document_returns_uuid(mock_create):
    mock_create.return_value = make_mock_client()
    from db.supabase_client import insert_document
    result = insert_document(
        filename="test.pdf",
        raw_text="Some text",
        description="A test document.",
        difficulty="Beginner",
        embedding=[0.1] * 384,
    )
    assert result == "test-uuid-1234"


@patch("db.supabase_client.create_client")
def test_insert_tags_called_with_correct_count(mock_create):
    client = make_mock_client()
    mock_create.return_value = client
    from db.supabase_client import insert_tags
    insert_tags("test-uuid-1234", SAMPLE_TAGS)
    # Should have called insert once with 4 rows (2 subjects + 2 skills)
    call_args = client.table.return_value.insert.call_args[0][0]
    assert len(call_args) == 4


@patch("db.supabase_client.create_client")
def test_delete_document_calls_delete(mock_create):
    client = make_mock_client()
    mock_create.return_value = client
    from db.supabase_client import delete_document
    delete_document("test-uuid-1234")
    client.table.return_value.delete.assert_called_once()


@patch("db.supabase_client.create_client")
def test_search_documents_calls_rpc(mock_create):
    mock_create.return_value = make_mock_client(rpc_return=[
        {"id": "abc", "filename": "notes.pdf", "description": "ML notes", "difficulty": "Intermediate", "similarity": 0.92}
    ])
    from db.supabase_client import search_documents
    results = search_documents([0.1] * 384)
    assert isinstance(results, list)


@patch("db.supabase_client.create_client")
def test_get_all_tags_returns_dict(mock_create):
    client = make_mock_client(select_return=[
        {"tag_type": "subject", "name": "Mathematics"},
        {"tag_type": "skill", "name": "Eigenvalues"},
    ])
    mock_create.return_value = client
    from db.supabase_client import get_all_tags
    result = get_all_tags()
    assert "subject" in result
    assert "skill" in result
