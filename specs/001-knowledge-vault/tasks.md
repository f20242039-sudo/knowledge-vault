# Knowledge Vault — Tasks

> Generated from: `specs/001-knowledge-vault/plan.md`
> Ordered by dependency. Parallel groups can be worked simultaneously.

---

## Phase 1 — Foundation (sequential)

### TASK-001 · Project bootstrap
**Depends on:** nothing
**Parallelizable with:** nothing

- [ ] Create project directory structure as defined in `plan.md`
- [ ] Create `requirements.txt` with all dependencies
- [ ] Create `.env.example` with required env var names
- [ ] Create `.gitignore` (exclude `.env`, `__pycache__`, `.venv`)
- [ ] Initialize git repo

**Deliverable:** Runnable empty project that imports without errors.

---

### TASK-002 · Supabase schema setup
**Depends on:** TASK-001
**Parallelizable with:** TASK-003, TASK-004

- [ ] Enable `pgvector` extension in Supabase dashboard
- [ ] Write `db/migrations/001_initial_schema.sql` with `documents` and `tags` tables
- [ ] Run migration in Supabase SQL editor
- [ ] Verify tables exist and pgvector index works

**Deliverable:** `001_initial_schema.sql` + confirmed tables in Supabase.

---

### TASK-003 · Text extraction module
**Depends on:** TASK-001
**Parallelizable with:** TASK-002, TASK-004

- [ ] Implement `utils/extractors.py`:
  - `extract_pdf(file_bytes) -> str` using PyMuPDF
  - `extract_docx(file_bytes) -> str` using python-docx
  - `extract_txt(file_bytes) -> str`
  - `extract(file_bytes, filename) -> str` — router function
- [ ] Handle empty/unreadable files gracefully (return empty string + log warning)
- [ ] Write `tests/test_extractors.py` with sample files

**Deliverable:** `utils/extractors.py` with passing tests.

---

### TASK-004 · Pydantic schema for AI output
**Depends on:** TASK-001
**Parallelizable with:** TASK-002, TASK-003

- [ ] Implement `ai/schemas.py`:
  - `SkillTag(name: str, coverage: int)`
  - `DocumentTagSchema(description, difficulty, subjects, skills)`
- [ ] Add validators: coverage 0–100, difficulty in allowed set
- [ ] Test parsing valid and invalid Claude JSON responses

**Deliverable:** `ai/schemas.py` with Pydantic models and validation tests.

---

## Phase 2 — AI Pipeline (parallel group)

### TASK-005 · Claude tagging module
**Depends on:** TASK-004
**Parallelizable with:** TASK-006

- [ ] Write `ai/prompts/tag_document.txt` — Claude prompt template
- [ ] Implement `ai/claude_tagger.py`:
  - `tag_document(text: str) -> DocumentTagSchema`
  - Truncate text to 6000 chars before sending
  - Parse JSON from Claude response
  - Validate with Pydantic schema
  - Retry up to 2 times on API error
- [ ] Write `tests/test_tagger.py` with mocked Claude responses

**Deliverable:** `ai/claude_tagger.py` that takes raw text, returns validated tags.

---

### TASK-006 · Embedding module
**Depends on:** TASK-001
**Parallelizable with:** TASK-005

- [ ] Implement `ai/embedder.py`:
  - Load `all-MiniLM-L6-v2` model on first call (cached)
  - `embed(text: str) -> list[float]` — returns 384-dim vector
  - Truncate input to 512 tokens
- [ ] Write `tests/test_embedder.py` — verify output is 384-dim list of floats

**Deliverable:** `ai/embedder.py` with passing tests.

---

## Phase 3 — Database Layer

### TASK-007 · Supabase client
**Depends on:** TASK-002, TASK-004
**Parallelizable with:** nothing (other tasks depend on this)

- [ ] Implement `db/supabase_client.py`:
  - `insert_document(filename, file_path, raw_text, description, difficulty, embedding) -> str` (returns UUID)
  - `insert_tags(document_id, subjects: list[str], skills: list[SkillTag])`
  - `search_documents(query_vector, limit=10) -> list[dict]`
  - `get_all_documents() -> list[dict]`
  - `get_document_by_id(id) -> dict`
  - `delete_document(id)`
  - `get_documents_by_tag(tag_type, tag_name) -> list[dict]`
- [ ] Write `tests/test_db.py` with mocked Supabase client

**Deliverable:** `db/supabase_client.py` covering all read/write operations.

---

## Phase 4 — Pipeline Orchestration

### TASK-008 · Ingest pipeline
**Depends on:** TASK-003, TASK-005, TASK-006, TASK-007

- [ ] Implement `pipeline/ingest.py`:
  - `ingest_document(file_bytes, filename) -> dict`
    1. Extract text via `extractors.extract()`
    2. Tag via `claude_tagger.tag_document()`
    3. Embed via `embedder.embed()`
    4. Store via `supabase_client.insert_document()` + `insert_tags()`
    5. Return document ID and tag summary
- [ ] Raise descriptive errors at each step
- [ ] Write integration test with mocked AI and DB

**Deliverable:** `pipeline/ingest.py` — the single function the UI calls on upload.

---

## Phase 5 — Streamlit UI

### TASK-009 · Upload page
**Depends on:** TASK-008

- [ ] Build upload UI in `app.py` or `pages/upload.py`:
  - File uploader (PDF, TXT, DOCX)
  - Progress spinner during processing
  - Success message with tag summary on completion
  - Error message on failure (never crash silently)

**Deliverable:** Working upload flow in Streamlit.

---

### TASK-010 · Library browse page
**Depends on:** TASK-007
**Parallelizable with:** TASK-009

- [ ] Build library page:
  - List all documents with filename, difficulty badge, subject tags
  - Click a document → show full tag profile
  - Delete button per document with confirmation

**Deliverable:** Library page showing all uploaded documents with tags.

---

### TASK-011 · Search page
**Depends on:** TASK-007, TASK-006
**Parallelizable with:** TASK-009, TASK-010

- [ ] Build search page:
  - Text input for semantic query
  - Embed the query string on submit
  - Display ranked results with similarity score and tags
  - "No results" empty state

**Deliverable:** Semantic search returning ranked documents.

---

### TASK-012 · Tag filter page
**Depends on:** TASK-007
**Parallelizable with:** TASK-009, TASK-010, TASK-011

- [ ] Build tag browser:
  - List all unique subjects and skills as clickable filters
  - Selecting a tag shows all matching documents

**Deliverable:** Tag filter sidebar or page.

---

## Phase 6 — Polish & Wrap-up

### TASK-013 · End-to-end smoke test
**Depends on:** TASK-009 through TASK-012

- [ ] Upload 5 diverse documents (math PDF, ML notes, Python tutorial)
- [ ] Verify each has correct subjects, skills, difficulty
- [ ] Run semantic search — confirm relevant results
- [ ] Delete a document — confirm it's gone from all views

---

### TASK-014 · Documentation
**Depends on:** TASK-013

- [ ] Write `README.md` with setup instructions
- [ ] Document env vars in `.env.example`
- [ ] Add inline comments to all pipeline modules

---

## Task Summary

| Phase | Tasks | Parallel? |
|---|---|---|
| 1 — Foundation | 001–004 | 002, 003, 004 parallel after 001 |
| 2 — AI Pipeline | 005–006 | Fully parallel |
| 3 — DB Layer | 007 | Blocks phase 4 |
| 4 — Orchestration | 008 | Sequential |
| 5 — UI | 009–012 | Fully parallel |
| 6 — Polish | 013–014 | Sequential |
