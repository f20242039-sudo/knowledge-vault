# Knowledge Vault — Data Model

---

## Overview

The data model has two concerns:
1. **Structured metadata** (document info, tags, difficulty) — stored in PostgreSQL tables
2. **Semantic vectors** (document embeddings for similarity search) — stored as a `VECTOR(384)` column via pgvector

Both live in the same Supabase project, in the same `public` schema.

---

## Entity: Document

Represents one uploaded file after processing.

| Column | Type | Nullable | Description |
|---|---|---|---|
| `id` | UUID | No | Primary key, auto-generated |
| `filename` | TEXT | No | Original filename (e.g. `Linear Algebra Notes.pdf`) |
| `file_path` | TEXT | Yes | Path in Supabase Storage bucket |
| `raw_text` | TEXT | Yes | Full extracted plain text |
| `description` | TEXT | Yes | AI-generated 2–3 sentence overview |
| `difficulty` | TEXT | Yes | One of: `Beginner`, `Intermediate`, `Advanced` |
| `embedding` | VECTOR(384) | Yes | sentence-transformers embedding of raw text |
| `created_at` | TIMESTAMPTZ | No | Upload timestamp |

---

## Entity: Tag

Represents a single subject or skill tag attached to a document.

| Column | Type | Nullable | Description |
|---|---|---|---|
| `id` | UUID | No | Primary key |
| `document_id` | UUID | No | FK → `documents.id` (CASCADE DELETE) |
| `tag_type` | TEXT | No | Either `subject` or `skill` |
| `name` | TEXT | No | Tag label (e.g. `Gradient descent`) |
| `coverage` | INTEGER | Yes | 0–100. For skills: % of concept covered. For subjects: NULL or 100 |

---

## Relationships

```
documents (1) ──< tags (many)
```

One document has many tags. Deleting a document cascades to delete its tags.

---

## Tag Taxonomy

### Subject tags (AI-inferred, not a fixed list)
Examples: `Mathematics`, `Machine Learning`, `Programming`, `Physics`, `Statistics`, `Data Science`, `Computer Science`, `Linear Algebra`, `Calculus`

### Skill tags (AI-inferred, granular)
Examples: `Matrix operations`, `Eigenvalues`, `Gradient descent`, `Backpropagation`, `NumPy`, `Data cleaning`, `Pandas`, `Neural networks`, `Probability`, `Bayes theorem`

### Difficulty (fixed enum)
- `Beginner` — assumes no prior knowledge of the subject
- `Intermediate` — assumes foundational knowledge, introduces complexity
- `Advanced` — assumes strong domain expertise, research-level or highly technical

---

## SQL Migration

```sql
-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Documents table
CREATE TABLE documents (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  filename    TEXT NOT NULL,
  file_path   TEXT,
  raw_text    TEXT,
  description TEXT,
  difficulty  TEXT CHECK (difficulty IN ('Beginner', 'Intermediate', 'Advanced')),
  embedding   VECTOR(384),
  created_at  TIMESTAMPTZ DEFAULT now()
);

-- Tags table
CREATE TABLE tags (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  document_id UUID NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
  tag_type    TEXT NOT NULL CHECK (tag_type IN ('subject', 'skill')),
  name        TEXT NOT NULL,
  coverage    INTEGER CHECK (coverage BETWEEN 0 AND 100)
);

-- Indexes
CREATE INDEX idx_tags_document_id ON tags(document_id);
CREATE INDEX idx_tags_type_name   ON tags(tag_type, name);
CREATE INDEX idx_documents_embed  ON documents USING ivfflat (embedding vector_cosine_ops)
  WITH (lists = 100);
```

---

## Pydantic Schema (Python-side validation)

```python
from pydantic import BaseModel, field_validator
from typing import Literal

class SkillTag(BaseModel):
    name: str
    coverage: int

    @field_validator('coverage')
    def coverage_range(cls, v):
        assert 0 <= v <= 100, "Coverage must be 0–100"
        return v

class DocumentTagSchema(BaseModel):
    description: str
    difficulty: Literal['Beginner', 'Intermediate', 'Advanced']
    subjects: list[str]
    skills: list[SkillTag]
```

---

## Sample Data

**Document:** `Neural Networks Lecture 3.pdf`

```json
{
  "id": "a1b2c3d4-...",
  "filename": "Neural Networks Lecture 3.pdf",
  "description": "A lecture covering the mathematics of backpropagation, chain rule application in multilayer perceptrons, and an introduction to vanishing gradients.",
  "difficulty": "Intermediate",
  "embedding": [0.023, -0.041, ...],  // 384 floats
  "tags": [
    { "tag_type": "subject", "name": "Machine Learning",   "coverage": null },
    { "tag_type": "subject", "name": "Mathematics",        "coverage": null },
    { "tag_type": "skill",   "name": "Backpropagation",    "coverage": 90 },
    { "tag_type": "skill",   "name": "Gradient descent",   "coverage": 70 },
    { "tag_type": "skill",   "name": "Chain rule",         "coverage": 85 },
    { "tag_type": "skill",   "name": "Vanishing gradients","coverage": 40 }
  ]
}
```
