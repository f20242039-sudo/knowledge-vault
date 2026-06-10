# Knowledge Vault — Research

> Technology choices investigated, alternatives considered, and decisions recorded.

---

## Vector Database Options

### Evaluated

| Option | Pros | Cons | Decision |
|---|---|---|---|
| **Supabase + pgvector** | SQL + vector in one service, free tier, managed | Slightly slower than dedicated vector DBs at massive scale | ✅ **Chosen** |
| Pinecone | Purpose-built, fast at scale | Separate from relational DB, costs money at scale | ❌ Adds complexity |
| Chroma | Local, zero setup, great for prototyping | No cloud sync, not production-ready | ❌ Too local |
| Weaviate | Feature-rich, hybrid search | Heavy to self-host, overkill for v1 | ❌ Overkill |
| Qdrant | Fast, open source | Separate from relational data | ❌ Adds complexity |

**Decision:** Supabase keeps relational metadata and vector search in one place. The pgvector `<=>` (cosine) operator is sufficient for our scale (hundreds to low thousands of documents).

---

## Embedding Model Options

### Evaluated

| Model | Dimensions | Size | Speed | Quality | Decision |
|---|---|---|---|---|---|
| `all-MiniLM-L6-v2` | 384 | 80MB | Fast | Good | ✅ **Chosen** |
| `all-mpnet-base-v2` | 768 | 420MB | Slower | Better | ❌ Too heavy for v1 |
| OpenAI `text-embedding-3-small` | 1536 | API call | API latency | Excellent | ❌ Costs money, API dependency |
| `bge-small-en-v1.5` | 384 | 130MB | Fast | Good | Viable alternative |

**Decision:** `all-MiniLM-L6-v2` runs locally (no API cost), is fast enough for synchronous Streamlit use, and 384 dimensions works well with pgvector.

---

## AI Tagging — Model Choice

**Claude `claude-sonnet-4-20250514`** chosen for tagging because:
- Reliably returns valid JSON when instructed
- Understands academic and technical documents across domains
- Accurately infers difficulty level without examples
- Coverage percentages are meaningfully calibrated

**Prompt strategy:** Send first 6000 characters of extracted text with an explicit JSON schema in the system prompt. Validate response with Pydantic before any DB write.

---

## UI Framework Options

| Option | Pros | Cons | Decision |
|---|---|---|---|
| **Streamlit** | Pure Python, file upload built-in, fast to build | Limited custom styling | ✅ **Chosen** |
| Gradio | Similar to Streamlit | Fewer layout options | ❌ Less flexible |
| FastAPI + React | Full control | Requires JS frontend | ❌ Too much overhead for v1 |
| Flask + Jinja | Lightweight | Manual everything | ❌ Tedious |

---

## PDF Parsing Options

| Library | Handles complex PDFs | Speed | Decision |
|---|---|---|---|
| **PyMuPDF (fitz)** | Yes | Fast | ✅ **Chosen** |
| pdfplumber | Good | Medium | Viable alternative |
| pypdf | Basic | Fast | ❌ Misses formatted text |
| pdfminer | Detailed | Slow | ❌ Too slow |

---

## Speckit Workflow Fit

Speckit's 7-step workflow maps naturally onto this project:

| Speckit Step | Knowledge Vault Output |
|---|---|
| `specify init` | Project folder + `.specify/` scaffold |
| `/speckit.constitution` | `.specify/memory/constitution.md` — coding standards, principles |
| `/speckit.specify` | `specs/001-knowledge-vault/spec.md` — user stories |
| `/speckit.clarify` | Q&A resolved: auth deferred, chunk embeddings deferred, v1 scope confirmed |
| `/speckit.plan` | `specs/001-knowledge-vault/plan.md` — tech stack + architecture |
| `/speckit.tasks` | `specs/001-knowledge-vault/tasks.md` — 14 ordered tasks |
| `/speckit.implement` | Claude Code executes TASK-001 through TASK-014 |

---

## Open Questions (resolved)

**Q: Should we chunk documents for better retrieval granularity?**
A: No for v1. One embedding per document keeps the system simple. Chunk-level embeddings deferred to v2.

**Q: Should we support multi-user accounts?**
A: No for v1. Single-user prototype. Auth can be added in v2 via Supabase Auth.

**Q: Should Claude re-rank search results?**
A: No for v1. pgvector cosine similarity is sufficient. Re-ranking would add latency and cost.

**Q: What's the maximum document size we support?**
A: v1 will truncate to 6000 characters for tagging and 512 tokens for embedding. Full text is stored but not fully embedded.
