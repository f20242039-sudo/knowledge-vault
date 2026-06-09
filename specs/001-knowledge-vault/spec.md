# Knowledge Vault — Spec

> **Rule:** This document describes WHAT the system does and WHY. No technology decisions here.

---

## Problem Statement

Students, researchers, and knowledge workers accumulate large numbers of documents — PDFs, lecture notes, articles, textbooks — but have no efficient way to find the right document when they need it. Manual tagging is tedious and inconsistent. Keyword search misses conceptually related content. The result: a growing pile of files that becomes harder to use over time.

---

## User Stories

### Core Upload & Organization

**US-01 — Upload a document**
As a user, I want to upload a PDF, text file, or document so that it enters my knowledge vault and becomes searchable.
*Acceptance:* Upload completes without error. The document appears in my library within a few seconds.

**US-02 — Automatic subject tagging**
As a user, I want the system to automatically identify which subjects a document covers (e.g. Mathematics, Machine Learning, Programming) so that I don't have to categorize it manually.
*Acceptance:* Every uploaded document gets at least one subject tag assigned without user input.

**US-03 — Automatic skill tagging**
As a user, I want the system to identify specific skills covered in a document (e.g. "gradient descent", "NumPy", "matrix operations") with a coverage percentage so that I know how deeply each skill is covered.
*Acceptance:* Each document has a list of skill tags, each with a coverage level (e.g. "covers 70% of this concept").

**US-04 — Difficulty inference**
As a user, I want each document tagged with a difficulty level (Beginner / Intermediate / Advanced) so that I can quickly find material appropriate to my current level.
*Acceptance:* Every document has exactly one difficulty tag.

**US-05 — View document profile**
As a user, I want to click on any document and see its full AI-generated profile: subject tags, skill tags, difficulty, and a short description of what the document covers.
*Acceptance:* A document detail view shows all tags and the AI-generated description.

---

### Search & Retrieval

**US-06 — Semantic search by concept**
As a user, I want to type a concept or question (e.g. "how does backpropagation work") and get back the documents most relevant to that concept, even if those exact words don't appear in the document.
*Acceptance:* Searching returns a ranked list of relevant documents. The top result is conceptually related even without exact keyword matches.

**US-07 — Filter by tag**
As a user, I want to filter my library by subject, skill, or difficulty so that I can browse a specific subset of my documents.
*Acceptance:* Selecting a tag shows only documents that carry that tag.

**US-08 — Multi-document relevance**
As a user, when I search for a topic, I want to receive *all* documents relevant to that query — not just the top one — so I can decide which to read.
*Acceptance:* Search returns multiple documents ranked by relevance, not just a single answer.

---

### Library Management

**US-09 — View full library**
As a user, I want to browse all documents I've uploaded in a list view with their tags visible so that I can get an overview of my vault.
*Acceptance:* The library page shows all documents with subject tags and difficulty level displayed.

**US-10 — Delete a document**
As a user, I want to remove a document from my vault so that my library stays clean.
*Acceptance:* Deleting a document removes it from the library, search results, and the database.

---

## Out of Scope (v1)
- User authentication / multi-user support
- OCR on scanned image PDFs
- Generating summaries of documents
- Editing or annotating documents inside the app
- Mobile app

---

## Success Criteria
- A user can upload 10 documents and have all of them fully tagged within 2 minutes
- A semantic search query returns at least one genuinely relevant document from a vault of 20 mixed documents
- A user who has never used the system can upload a file and find it via search within 5 minutes, with no instructions
