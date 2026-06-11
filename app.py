"""
app.py — Knowledge Vault
Run with: streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="Knowledge Vault",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,700&family=Outfit:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="collapsedControl"] { color: #c4b5fd !important; }

/* ── Palette
   bg-deep    : #1a0533   deep purple-black
   bg-card    : #230a42   slightly lighter purple
   bg-raised  : #2d1057   raised surfaces
   border     : #4a1f8a   violet border
   accent     : #9333ea   bright purple
   accent-lt  : #c4b5fd   soft lavender
   glow       : #7c3aed   medium violet
   text       : #f3e8ff   near-white lavender
   text-dim   : #a78bfa   muted lavender
   text-muted : #7c5cbf   very muted
── */

.stApp {
    background: linear-gradient(160deg, #1a0533 0%, #0f0221 50%, #1a0533 100%);
    min-height: 100vh;
}

[data-testid="stSidebar"] {
    background: #140328;
    border-right: 1px solid #4a1f8a;
}
[data-testid="stSidebar"] * { color: #f3e8ff !important; }

/* ── Hero ── */
.hero {
    padding: 3rem 0 0.5rem;
    text-align: center;
}
.hero-eyebrow {
    font-family: 'Outfit', sans-serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.25em;
    color: #9333ea;
    text-transform: uppercase;
    margin-bottom: 1rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 5.5rem;
    font-weight: 900;
    color: #f3e8ff;
    line-height: 1.0;
    margin: 0 0 0.5rem;
    letter-spacing: -0.02em;
}
.hero-title em {
    font-style: italic;
    font-weight: 700;
    background: linear-gradient(135deg, #9333ea 0%, #e879f9 50%, #c4b5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    color: #a78bfa;
    font-size: 1.15rem;
    font-weight: 300;
    margin-top: 0.75rem;
    letter-spacing: 0.01em;
}

/* ── Intro box ── */
.intro-box {
    background: linear-gradient(135deg, #2d1057 0%, #3b0f6e 100%);
    border: 1px solid #6d28d9;
    border-radius: 20px;
    padding: 2rem 2.5rem;
    margin: 2rem auto;
    max-width: 860px;
    position: relative;
    overflow: hidden;
}
.intro-box::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 160px; height: 160px;
    background: radial-gradient(circle, #9333ea22, transparent 70%);
    border-radius: 50%;
}
.intro-box::after {
    content: '';
    position: absolute;
    bottom: -30px; left: -30px;
    width: 120px; height: 120px;
    background: radial-gradient(circle, #e879f922, transparent 70%);
    border-radius: 50%;
}
.intro-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    font-weight: 900;
    color: #f3e8ff;
    margin-bottom: 0.75rem;
}
.intro-text {
    color: #c4b5fd;
    font-size: 1rem;
    line-height: 1.8;
    font-weight: 300;
}
.intro-steps {
    display: flex;
    gap: 1.5rem;
    margin-top: 1.5rem;
    flex-wrap: wrap;
}
.intro-step {
    flex: 1;
    min-width: 160px;
    background: #1a0533;
    border: 1px solid #4a1f8a;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    text-align: center;
}
.intro-step-icon {
    font-size: 1.8rem;
    margin-bottom: 0.4rem;
}
.intro-step-label {
    font-size: 0.8rem;
    font-weight: 600;
    color: #c4b5fd;
    letter-spacing: 0.03em;
}
.intro-step-desc {
    font-size: 0.75rem;
    color: #7c5cbf;
    margin-top: 0.2rem;
    font-weight: 300;
}

/* ── Nav icons ── */
.nav-section {
    display: flex;
    justify-content: center;
    gap: 1.2rem;
    margin: 2rem 0 1.5rem;
    flex-wrap: wrap;
}
.nav-icon-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    background: #230a42;
    border: 1px solid #4a1f8a;
    border-radius: 18px;
    padding: 1.4rem 2rem;
    cursor: pointer;
    transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s, border-color 0.2s, background 0.2s;
    min-width: 110px;
    text-decoration: none;
}
.nav-icon-btn:hover {
    transform: translateY(-8px);
    border-color: #9333ea;
    background: #2d1057;
    box-shadow: 0 16px 40px #9333ea33, 0 0 0 1px #9333ea44;
}
.nav-icon-btn.active {
    border-color: #9333ea;
    background: #2d1057;
    box-shadow: 0 0 0 2px #9333ea55;
}
.nav-icon {
    font-size: 2.2rem;
    line-height: 1;
}
.nav-label {
    font-size: 0.78rem;
    font-weight: 600;
    color: #c4b5fd;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* Streamlit button overrides for nav */
div[data-testid="column"] > div > div > div > div > .stButton > button {
    background: #230a42 !important;
    border: 1px solid #4a1f8a !important;
    border-radius: 18px !important;
    padding: 1.4rem 1rem !important;
    width: 100% !important;
    color: #c4b5fd !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
    transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s !important;
    box-shadow: none !important;
    height: auto !important;
    line-height: 1.4 !important;
}
div[data-testid="column"] > div > div > div > div > .stButton > button:hover {
    transform: translateY(-8px) !important;
    border-color: #9333ea !important;
    background: #2d1057 !important;
    box-shadow: 0 16px 40px #9333ea33 !important;
    color: #f3e8ff !important;
}

/* Primary button */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7c3aed, #9333ea) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    padding: 0.65rem 2rem !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 4px 24px #9333ea55 !important;
    transition: opacity 0.2s, box-shadow 0.2s, transform 0.15s !important;
}
.stButton > button[kind="primary"]:hover {
    opacity: 0.9 !important;
    box-shadow: 0 8px 32px #9333ea88 !important;
    transform: translateY(-2px) !important;
}

/* ── Cards ── */
.vault-card {
    background: #230a42;
    border: 1px solid #4a1f8a;
    border-radius: 18px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1rem;
    position: relative;
    transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s, border-color 0.2s;
    overflow: hidden;
}
.vault-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, #9333ea, #e879f9);
    opacity: 0;
    transition: opacity 0.2s;
}
.vault-card:hover {
    transform: translateY(-4px);
    border-color: #9333ea55;
    box-shadow: 0 12px 40px #9333ea22;
}
.vault-card:hover::before { opacity: 1; }

.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-weight: 900;
    color: #f3e8ff;
    margin-bottom: 6px;
}
.card-desc {
    color: #a78bfa;
    font-size: 0.88rem;
    line-height: 1.7;
    font-weight: 300;
}

/* ── Tags ── */
.tag-subject {
    display: inline-block;
    background: #2d1057;
    color: #e9d5ff;
    border: 1px solid #6d28d9;
    border-radius: 6px;
    padding: 3px 11px;
    font-size: 0.75rem;
    font-weight: 500;
    margin: 3px;
    letter-spacing: 0.02em;
}
.tag-skill {
    display: inline-block;
    background: #1a0533;
    color: #c4b5fd;
    border: 1px solid #4a1f8a;
    border-radius: 6px;
    padding: 3px 11px;
    font-size: 0.75rem;
    font-weight: 500;
    margin: 3px;
    letter-spacing: 0.02em;
}
.tag-difficulty-Beginner     { background:#0a2015; color:#6ee7b7; border:1px solid #166534; }
.tag-difficulty-Intermediate { background:#1c1000; color:#fcd34d; border:1px solid #854d0e; }
.tag-difficulty-Advanced     { background:#200a33; color:#e879f9; border:1px solid #6d28d9; }
.difficulty-badge {
    display: inline-block;
    border-radius: 8px;
    padding: 4px 13px;
    font-size: 0.73rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}

/* ── Progress bar ── */
.bar-bg {
    background: #2d1057;
    border-radius: 4px;
    height: 5px;
    width: 100%;
    margin-top: 6px;
}
.bar-fill {
    background: linear-gradient(90deg, #7c3aed, #e879f9);
    border-radius: 4px;
    height: 5px;
}

/* ── Utility ── */
.section-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    color: #7c5cbf;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}
.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 900;
    color: #f3e8ff;
    margin-bottom: 0.5rem;
}
.hint {
    color: #a78bfa;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
    font-weight: 300;
    line-height: 1.8;
}
.empty-state {
    color: #4a1f8a;
    font-size: 1rem;
    margin-top: 3rem;
    text-align: center;
    font-style: italic;
}

/* Input */
.stTextInput > div > div > input {
    background: #230a42 !important;
    border: 1px solid #4a1f8a !important;
    border-radius: 12px !important;
    color: #f3e8ff !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.7rem 1rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: #9333ea !important;
    box-shadow: 0 0 0 3px #9333ea33 !important;
}
.stTextInput > div > div > input::placeholder { color: #7c5cbf !important; }

/* File uploader */
[data-testid="stFileUploader"] {
    background: #230a42 !important;
    border: 1px dashed #4a1f8a !important;
    border-radius: 16px !important;
}
[data-testid="stFileUploader"]:hover { border-color: #9333ea !important; }

/* Expander */
details > summary {
    background: #230a42 !important;
    border: 1px solid #4a1f8a !important;
    border-radius: 14px !important;
    color: #f3e8ff !important;
    font-family: 'Playfair Display', serif !important;
    font-size: 1rem !important;
    font-weight: 900 !important;
    padding: 0.9rem 1.2rem !important;
}
details[open] > summary { border-radius: 14px 14px 0 0 !important; }
details > div {
    background: #1a0533 !important;
    border: 1px solid #4a1f8a !important;
    border-top: none !important;
    border-radius: 0 0 14px 14px !important;
    padding: 1rem 1.2rem !important;
}

hr { border-color: #2d1057 !important; }
.stSuccess { background: #0a2015 !important; border-color: #166534 !important; color: #6ee7b7 !important; border-radius: 12px !important; }
.stAlert { border-radius: 12px !important; }
</style>
""", unsafe_allow_html=True)


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class='hero'>
  <div class='hero-eyebrow'>✦ &nbsp; AI-Powered Document Library &nbsp; ✦</div>
  <div class='hero-title'>Knowledge <em>Vault</em></div>
  <div class='hero-sub'>Your documents, intelligently organised.</div>
</div>
""", unsafe_allow_html=True)

# ── Intro box ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class='intro-box'>
  <div class='intro-title'>How it works</div>
  <div class='intro-text'>
    Stop drowning in a sea of unsorted PDFs, lecture notes, and articles.
    Knowledge Vault reads every document you upload and automatically assigns it
    <strong style='color:#e9d5ff'>subject tags</strong>, <strong style='color:#e9d5ff'>skill tags</strong>,
    and a <strong style='color:#e9d5ff'>difficulty level</strong> — no manual effort needed.
    When you want to learn something new, just search for it and the vault surfaces
    exactly which documents to read, ranked by relevance.
  </div>
  <div class='intro-steps'>
    <div class='intro-step'>
      <div class='intro-step-icon'>📤</div>
      <div class='intro-step-label'>Upload</div>
      <div class='intro-step-desc'>Drop in any PDF, DOCX, or TXT</div>
    </div>
    <div class='intro-step'>
      <div class='intro-step-icon'>🤖</div>
      <div class='intro-step-label'>AI analyses</div>
      <div class='intro-step-desc'>Tags subjects, skills & difficulty</div>
    </div>
    <div class='intro-step'>
      <div class='intro-step-icon'>🔍</div>
      <div class='intro-step-label'>Search</div>
      <div class='intro-step-desc'>Find by concept, not just keyword</div>
    </div>
    <div class='intro-step'>
      <div class='intro-step-icon'>📚</div>
      <div class='intro-step-label'>Discover</div>
      <div class='intro-step-desc'>Know exactly what to read</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Nav ───────────────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Upload"

pages     = ["Upload", "Search", "Library", "Browse by Tag"]
icons     = ["📤", "🔍", "📚", "🏷️"]
nav_cols  = st.columns(4)

for i, (p, icon) in enumerate(zip(pages, icons)):
    with nav_cols[i]:
        label = f"{icon}\n\n{p}"
        if st.button(label, key=f"nav_{p}"):
            st.session_state.page = p

page = st.session_state.page
st.markdown("<hr style='margin:0.5rem 0 2rem'>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<div style='font-family:Playfair Display,serif;font-size:1.4rem;font-weight:900;color:#f3e8ff;padding:0.5rem 0 0.25rem'>✦ Knowledge Vault</div>", unsafe_allow_html=True)
    st.markdown("---")
    sb = st.radio("Navigate", pages, index=pages.index(page), label_visibility="collapsed")
    if sb != page:
        st.session_state.page = sb
        st.rerun()
    st.markdown("---")
    st.markdown("<div style='color:#4a1f8a;font-size:0.8rem;line-height:1.9;font-style:italic'>Upload once.<br>Find anything.<br>AI does the rest.</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# UPLOAD
# ══════════════════════════════════════════════════════════════════════════════
if page == "Upload":
    st.markdown("<div class='page-title'>Upload a document</div>", unsafe_allow_html=True)
    st.markdown("<div class='hint'>Drop in a PDF, DOCX, or TXT — the AI will read it and automatically assign subjects, skills, and difficulty level. No manual tagging needed.</div>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"], label_visibility="collapsed")

    if uploaded_file:
        st.markdown(f"<div style='color:#a78bfa;font-size:0.9rem;margin:0.6rem 0 0.9rem'>📄 &nbsp;{uploaded_file.name} &nbsp;·&nbsp; {uploaded_file.size // 1024} KB</div>", unsafe_allow_html=True)

        if st.button("✦ Analyse & Add to Vault", type="primary"):
            from pipeline.ingest import ingest_document
            file_bytes = uploaded_file.read()
            try:
                with st.spinner("Reading and analysing your document… (15–20 seconds)"):
                    result = ingest_document(file_bytes, uploaded_file.name)

                st.success(f"✓ Added to vault — {result.filename}")
                st.markdown("<br>", unsafe_allow_html=True)

                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown("<div class='section-label'>What this document covers</div>", unsafe_allow_html=True)
                    st.markdown(f"<div style='color:#a78bfa;line-height:1.8;font-size:0.95rem;font-weight:300'>{result.description}</div>", unsafe_allow_html=True)
                with col2:
                    diff_cls = f"tag-difficulty-{result.difficulty}"
                    st.markdown(f"<div class='section-label'>Level</div><span class='difficulty-badge {diff_cls}'>{result.difficulty}</span>", unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<div class='section-label'>Subjects</div>", unsafe_allow_html=True)
                st.markdown(" ".join(f"<span class='tag-subject'>{s}</span>" for s in result.subjects), unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<div class='section-label'>Skills detected</div>", unsafe_allow_html=True)
                for skill in sorted(result.skills, key=lambda x: x["coverage"], reverse=True):
                    c1, c2 = st.columns([2, 3])
                    with c1:
                        st.markdown(f"<span class='tag-skill'>{skill['name']}</span>", unsafe_allow_html=True)
                    with c2:
                        pct = skill["coverage"]
                        st.markdown(
                            f"<div class='bar-bg'><div class='bar-fill' style='width:{pct}%'></div></div>"
                            f"<div style='color:#6d28d9;font-size:0.7rem;margin-top:3px'>{pct}% coverage</div>",
                            unsafe_allow_html=True,
                        )
            except ValueError as e:
                st.error(f"Could not process file: {e}")
            except Exception as e:
                st.error(f"Something went wrong: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# SEARCH
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Search":
    st.markdown("<div class='page-title'>Search your vault</div>", unsafe_allow_html=True)
    st.markdown("<div class='hint'>Describe what you want to learn or find. The AI understands meaning — so searching \"how transformers work\" will surface your attention mechanism notes even if those exact words don't appear in the document.</div>", unsafe_allow_html=True)

    query = st.text_input("What topic or skill are you looking for?", placeholder="e.g.  gradient descent  ·  probability distributions  ·  how sorting algorithms work", label_visibility="collapsed")

    if query:
        from ai.embedder import embed
        from db.supabase_client import search_documents
        with st.spinner("Searching your vault…"):
            try:
                results = search_documents(embed(query), limit=10)
            except Exception as e:
                st.error(f"Search failed: {e}")
                results = []

        if not results:
            st.markdown("<div class='empty-state'>Nothing found — try uploading some documents first.</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='section-label' style='margin-bottom:1.2rem'>{len(results)} result{'s' if len(results)!=1 else ''} for &ldquo;{query}&rdquo;</div>", unsafe_allow_html=True)
            for doc in results:
                sim  = int(doc.get("similarity", 0) * 100)
                tags = doc.get("tags", [])
                subj = [t["name"] for t in tags if t["tag_type"] == "subject"]
                skls = [t["name"] for t in tags if t["tag_type"] == "skill"]
                diff = doc.get("difficulty", "")
                dcls = f"tag-difficulty-{diff}"
                st.markdown(f"""
                <div class='vault-card'>
                  <div style='display:flex;justify-content:space-between;align-items:flex-start;gap:1rem'>
                    <div style='flex:1'>
                      <div class='card-title'>{doc['filename']}</div>
                      <div class='card-desc'>{doc.get('description','')}</div>
                    </div>
                    <span class='difficulty-badge {dcls}'>{diff}</span>
                  </div>
                  <div style='margin-top:1rem'>
                    {"".join(f"<span class='tag-subject'>{s}</span>" for s in subj)}
                    {"".join(f"<span class='tag-skill'>{s}</span>" for s in skls[:6])}
                  </div>
                  <div style='margin-top:1rem'>
                    <div style='color:#6d28d9;font-size:0.7rem;letter-spacing:0.1em;font-weight:600'>RELEVANCE &nbsp; {sim}%</div>
                    <div class='bar-bg'><div class='bar-fill' style='width:{sim}%'></div></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# LIBRARY
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Library":
    st.markdown("<div class='page-title'>Your library</div>", unsafe_allow_html=True)
    from db.supabase_client import get_all_documents, delete_document
    try:
        docs = get_all_documents()
    except Exception as e:
        st.error(f"Could not load library: {e}")
        docs = []

    if not docs:
        st.markdown("<div class='empty-state'>Your vault is empty.<br>Head to Upload to add your first document.</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='section-label'>{len(docs)} document{'s' if len(docs)!=1 else ''} in your vault</div>", unsafe_allow_html=True)
        for doc in docs:
            tags = doc.get("tags", [])
            subj = [t["name"] for t in tags if t["tag_type"] == "subject"]
            skls = [t["name"] for t in tags if t["tag_type"] == "skill"]
            diff = doc.get("difficulty", "")
            dcls = f"tag-difficulty-{diff}"
            with st.expander(f"  {doc['filename']}", expanded=False):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"<div class='card-desc' style='margin-bottom:1.2rem'>{doc.get('description','No description.')}</div>", unsafe_allow_html=True)
                    st.markdown("<div class='section-label'>Subjects</div>" + " ".join(f"<span class='tag-subject'>{s}</span>" for s in subj), unsafe_allow_html=True)
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown("<div class='section-label'>Skills</div>" + " ".join(f"<span class='tag-skill'>{s}</span>" for s in skls), unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<span class='difficulty-badge {dcls}'>{diff}</span>", unsafe_allow_html=True)
                    st.markdown("")
                    if st.button("Delete", key=f"del_{doc['id']}"):
                        try:
                            delete_document(doc["id"])
                            st.success("Deleted.")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Delete failed: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# BROWSE BY TAG
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Browse by Tag":
    st.markdown("<div class='page-title'>Browse by tag</div>", unsafe_allow_html=True)
    from db.supabase_client import get_all_tags, get_documents_by_tag
    try:
        all_tags = get_all_tags()
    except Exception as e:
        st.error(f"Could not load tags: {e}")
        all_tags = {"subject": [], "skill": []}

    cl, cr = st.columns([1, 2])
    with cl:
        st.markdown("<div class='section-label'>By subject</div>", unsafe_allow_html=True)
        sel_sub = st.radio("Subject", ["(all)"] + all_tags["subject"], label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='section-label'>By skill</div>", unsafe_allow_html=True)
        sel_skl = st.radio("Skill", ["(all)"] + all_tags["skill"], label_visibility="collapsed")

    with cr:
        active = None
        if sel_sub != "(all)":
            active = ("subject", sel_sub)
        elif sel_skl != "(all)":
            active = ("skill", sel_skl)

        if active:
            try:
                docs = get_documents_by_tag(*active)
            except Exception as e:
                st.error(f"Filter failed: {e}")
                docs = []
            _, tag_name = active
            st.markdown(f"<div class='section-label'>Tagged &mdash; {tag_name}</div>", unsafe_allow_html=True)
            if not docs:
                st.markdown("<div class='empty-state'>No documents with this tag yet.</div>", unsafe_allow_html=True)
            else:
                for doc in docs:
                    tags = doc.get("tags", [])
                    subj = [t["name"] for t in tags if t["tag_type"] == "subject"]
                    skls = [t["name"] for t in tags if t["tag_type"] == "skill"]
                    diff = doc.get("difficulty", "")
                    dcls = f"tag-difficulty-{diff}"
                    st.markdown(f"""
                    <div class='vault-card'>
                      <div style='display:flex;justify-content:space-between;gap:1rem'>
                        <div class='card-title'>{doc['filename']}</div>
                        <span class='difficulty-badge {dcls}'>{diff}</span>
                      </div>
                      <div class='card-desc'>{doc.get('description','')}</div>
                      <div style='margin-top:0.9rem'>
                        {"".join(f"<span class='tag-subject'>{s}</span>" for s in subj)}
                        {"".join(f"<span class='tag-skill'>{s}</span>" for s in skls)}
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown("<div class='empty-state'>Select a subject or skill on the left to filter your vault.</div>", unsafe_allow_html=True)
