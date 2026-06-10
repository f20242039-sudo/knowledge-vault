# Knowledge Vault — Technical Plan

> **Rule:** This document describes HOW we build it. Tech stack, architecture, and component decisions live here.

---

## Tech Stack

| Layer | Technology | Reason |
|---|---|---|
| UI | Streamlit (Python) | Rapid prototyping, file upload built-in, no JS needed |
| AI tagging | Anthropic Claude API (`claude-sonnet-4-20250514`) | Structured JSON output, best-in-class instruction following |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`) | Free, local, 384-dim, fast |
| Vector + DB | Supabase (PostgreSQL + pgvector) | One service for both relational metadata and vector search |
| File storage | Supabase Storage | Co-located with DB, S3-compatible |
| PDF parsing | PyMuPDF (`fitz`) | Fast, handles complex PDFs |
| DOCX parsing | `python-docx` | Standard library for Word files |
| Validation | Pydantic v2 | Enforce Claude's JSON output schema |
| Workflow | Speckit | Structured AI-assisted development methodology |
| Config | `python-dotenv` | Secret management |
| Testing | `pytest` | Standard Python testing |

---

## System Architecture

```
User Browser
    │
    ▼
┌─────────────────────────────────┐
│         Streamlit App           │  app.py
│  Upload │ Search │ Browse │ View │
└────────────────┬────────────────┘
                 │
    ┌────────────▼────────────┐
    │   Document Pipeline     │  pipeline/ingest.py
    │                         │
    │  1. Extract text        │  ← utils/extractors.py
    │  2. Call Claude API     │  ← ai/claude_tagger.py
    │  3. Validate tags       │  ← ai/schemas.py (Pydantic)
    │  4. Generate embedding  │  ← ai/embedder.py
    │  5. Store everything    │  ← db/supabase_client.py
    └─────────────────────────┘
                 │
    ┌────────────▼────────────┐
    │        Supabase         │
    │                         │
    │  PostgreSQL             │
    │  ├── documents table    │
    │  ├── tags table         │
    │  └── embeddings col     │  (pgvector)
    │                         │
    │  Storage bucket         │
    │  └── raw file blobs     │
    └─────────────────────────┘
```

---

## Database Schema

### `documents` table
```sql
CREATE TABLE documents (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  filename    TEXT NOT NULL,
  file_path   TEXT,                    -- Supabase Storage path
  raw_text    TEXT,                    -- extracted plain text
  description TEXT,                    -- AI-generated 2-3 sentence overview
  difficulty  TEXT CHECK (difficulty IN ('Beginner','Intermediate','Advanced')),
  embedding   VECTOR(384),             -- sentence-transformers all-MiniLM-L6-v2
  created_at  TIMESTAMPTZ DEFAULT now()
);
```

### `tags` table
```sql
CREATE TABLE tags (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID REFERENCES documents(id) ON DELETE CASCADE,
  tag_type    TEXT CHECK (tag_type IN ('subject','skill')),
  name        TEXT NOT NULL,
  coverage    INTEGER CHECK (coverage BETWEEN 0 AND 100)  -- % coverage
);

CREATE INDEX ON tags(document_id);
CREATE INDEX ON tags(tag_type, name);
```

### pgvector similarity search
```sql
-- Enable extension (run once)
CREATE EXTENSION IF NOT EXISTS vector;

-- Semantic search query
SELECT id, filename, description, difficulty,
       1 - (embedding <=> '[…query_vector…]') AS similarity
FROM documents
ORDER BY embedding <=> '[…query_vector…]'
LIMIT 10;
```

---

## AI Tagging — Claude Prompt Contract

Claude is called once per document with the extracted text. It returns a structured JSON object matching this schema:

```json
{
  "description": "2-3 sentence plain-English overview of the document.",
  "difficulty": "Beginner | Intermediate | Advanced",
  "subjects": ["Mathematics", "Machine Learning"],
  "skills": [
    { "name": "Gradient descent", "coverage": 85 },
    { "name": "Backpropagation", "coverage": 60 }
  ]
}
```

- `coverage` is 0–100 representing how thoroughly the document covers that skill.
- The Pydantic model `DocumentTagSchema` in `ai/schemas.py` validates this before any DB write.

---

## File Structure

```
knowledge-vault/
├── app.py                        # Streamlit entry point
├── .env                          # API keys (gitignored)
├── requirements.txt
│
├── .specify/                     # Speckit workflow files
│   ├── memory/
│   │   └── constitution.md
│   ├── scripts/bash/
│   │   ├── setup.sh
│   │   └── run_tests.sh
│   └── templates/
│       ├── spec_template.md
│       └── task_template.md
│
├── specs/                        # Speckit specs
│   └── 001-knowledge-vault/
│       ├── spec.md
│       ├── plan.md               ← this file
│       ├── tasks.md
│       ├── data-model.md
│       └── research.md
│
├── pipeline/
│   └── ingest.py                 # Orchestrates the full upload pipeline
│
├── ai/
│   ├── claude_tagger.py          # Claude API call + response parsing
│   ├── embedder.py               # sentence-transformers embedding
│   ├── schemas.py                # Pydantic models for AI output
│   └── prompts/
│       └── tag_document.txt      # Claude prompt template
│
├── db/
│   ├── supabase_client.py        # All DB read/write operations
│   └── migrations/
│       └── 001_initial_schema.sql
│
├── utils/
│   └── extractors.py             # PDF, DOCX, TXT text extraction
│
└── tests/
    ├── test_extractors.py
    ├── test_tagger.py
    ├── test_embedder.py
    └── test_db.py
```

---

## Embedding Strategy

- Model: `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions, runs locally)
- Input to embed: first 512 tokens of extracted text (sufficient for topic representation)
- Similarity metric: cosine similarity via pgvector `<=>` operator
- At query time: user's search string is embedded with the same model, then compared against all document vectors

---

## Key Design Decisions

| Decision | Choice | Rationale |
|---|---|---|
| One embedding per document | Yes | Simpler; sufficient for document-level retrieval |
| Chunk-level embeddings | No (v1) | Adds complexity; defer to v2 |
| Claude for re-ranking | No (v1) | pgvector cosine similarity is sufficient initially |
| Multi-user auth | No (v1) | Out of scope; single-user local prototype |
| Async pipeline | No (v1) | Streamlit's threading model; keep sync for simplicity |
