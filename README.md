# ✦ Knowledge Vault

**An AI-powered document library that organises your notes, PDFs, and articles automatically.**

Upload a document. The AI reads it, tags it with subjects, skills, and a difficulty level, and makes it instantly searchable by meaning — not just keywords.

---

## What it does

Most people accumulate hundreds of lecture notes, PDFs, and articles with no way to find the right one when they need it. Knowledge Vault solves this by letting AI do the organisation:

- **Upload** a PDF, DOCX, or TXT file
- **AI analyses** the content and assigns subject tags (e.g. *Machine Learning*, *Mathematics*), skill tags (e.g. *Gradient descent*, *Fourier Transform*) with coverage percentages, and a difficulty level (Beginner / Intermediate / Advanced)
- **Search semantically** — type "how does backpropagation work" and the vault surfaces relevant documents even if those exact words never appear in the file
- **Browse by tag** — filter your entire library by subject or skill
- **Switch languages** — the UI supports English, Telugu (తెలుగు), and Hindi (हिंदी)

---

## Tech stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| AI tagging | Groq API (`llama-3.3-70b-versatile`) or Ollama (local) |
| Embeddings | `sentence-transformers` — `all-MiniLM-L6-v2` (runs locally) |
| Database | Supabase (PostgreSQL + pgvector) |
| File parsing | PyMuPDF, python-docx |
| Validation | Pydantic v2 |
| Workflow | Speckit |

---

## Project structure

```
knowledge-vault/
├── app.py                        # Streamlit UI — all pages and sidebar
├── i18n.py                       # Translations (EN / TE / HI)
├── requirements.txt
├── .env                          # API keys (never committed)
│
├── pipeline/
│   └── ingest.py                 # Orchestrates extract → tag → embed → store
│
├── ai/
│   ├── groq_tagger.py            # Groq API tagging
│   ├── tagger.py                 # Unified router (Groq or Ollama)
│   ├── embedder.py               # Local sentence-transformers embedding
│   ├── schemas.py                # Pydantic models for AI output
│   └── prompts/
│       └── tag_document.txt      # Claude/Groq prompt template
│
├── db/
│   ├── supabase_client.py        # All DB read/write operations
│   └── migrations/
│       ├── 001_initial_schema.sql
│       └── 002_verify_schema.sql
│
├── utils/
│   ├── extractors.py             # PDF, DOCX, TXT text extraction
│   └── secrets.py                # Reads from .env or Streamlit secrets
│
├── tests/
│   ├── test_extractors.py
│   ├── test_tagger.py
│   ├── test_embedder.py
│   ├── test_db.py
│   └── test_ingest.py
│
└── .specify/                     # Speckit workflow files
    ├── memory/constitution.md
    └── specs/001-knowledge-vault/
        ├── spec.md
        ├── plan.md
        ├── tasks.md
        ├── data-model.md
        └── research.md
```

---

## Setup

### Prerequisites
- Python 3.11+
- A [Supabase](https://supabase.com) account (free tier works)
- A [Groq](https://console.groq.com) API key (free tier works), or Ollama running locally

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/knowledge-vault.git
cd knowledge-vault
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

The first run will download the sentence-transformers model (~80MB). This is cached after the first download.

### 3. Set up Supabase

1. Create a new Supabase project at [supabase.com](https://supabase.com)
2. Go to **SQL Editor** and run `db/migrations/001_initial_schema.sql`
3. Go to **Table Editor** and disable Row Level Security on both `documents` and `tags` tables (or run `ALTER TABLE documents DISABLE ROW LEVEL SECURITY;`)
4. Copy your **Project URL** and **anon key** from **Settings → API**

### 4. Create your `.env` file

```
SUPABASE_URL=https://xxxxxxxxxxxx.supabase.co
SUPABASE_KEY=eyJ...
GROQ_API_KEY=gsk_...
```

### 5. Run locally

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## Running tests

```bash
pytest tests/ -v
```

All tests mock external APIs — no real Groq or Supabase calls are made during testing.

---

## Deployment (Streamlit Cloud)

1. Push your repo to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set the main file to `app.py`
4. Under **Advanced settings → Secrets**, add:

```toml
SUPABASE_URL = "https://xxxxxxxxxxxx.supabase.co"
SUPABASE_KEY = "eyJ..."
GROQ_API_KEY = "gsk_..."
```

5. Click **Deploy**

---

## AI provider options

The sidebar lets you switch between two AI backends without touching any code:

**Groq (Cloud)** — fast, free-tier available. Uses `llama-3.3-70b-versatile`. You can enter your own API key (BYOK) directly in the sidebar.

**Ollama (Local)** — runs entirely on your machine, no API key needed. Requires [Ollama](https://ollama.com) installed and a model pulled:
```bash
ollama pull llama3.2
```

---

## How semantic search works

When a document is uploaded, the pipeline:
1. Extracts plain text from the file
2. Sends the text to the AI (Groq or Ollama) → receives structured JSON with subjects, skills, difficulty, and a description
3. Converts the text into a 384-dimensional vector using `all-MiniLM-L6-v2`
4. Stores the document, tags, and vector in Supabase

When a user searches, the query is embedded with the same model and compared against all document vectors using cosine similarity via pgvector. Documents are returned ranked by relevance — no exact keyword matching needed.

---

## Language support

The UI is available in three languages, switchable from the sidebar:

| Language | Script |
|---|---|
| English | Latin |
| Telugu | తెలుగు |
| Hindi | हिंदी |

Document content, stored tags, and AI prompts are always in English. Translation is display-only.

---

## Speckit workflow

This project was built using the [Speckit](https://speckit.dev) methodology — a structured AI-assisted development workflow. The full spec, technical plan, task breakdown, data model, and research are in `.specify/specs/001-knowledge-vault/`.

---

## Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Run tests before committing: `pytest tests/ -v`
4. Open a pull request

---

## Feedback

If you've used Knowledge Vault and want to share feedback, fill out the [review form](https://docs.google.com/forms/d/e/1FAIpQLSd0vCbRpt_d0VluB1axjA4skCcmr-TA3eJ1A0RdWxt8PTYB1Q/viewform?usp=publish-editor).
