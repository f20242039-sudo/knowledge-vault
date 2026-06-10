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
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Outfit:wght@300;400;500;600&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
#MainMenu, footer, header   { visibility: hidden; }
[data-testid="collapsedControl"] { color: #9d7dea !important; }

/* ── Palette
   obsidian-base : #09070f
   obsidian-card : #110e1c
   obsidian-raised: #181228
   border        : #251b3e
   violet        : #7c3aed
   violet-glow   : #9d5fff
   lavender      : #c4b5fd
   muted         : #6b5a8e
   text          : #ede9fe
   text-dim      : #9b8db5
── */

.stApp { background: #09070f; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0d0a18;
    border-right: 1px solid #251b3e;
}
[data-testid="stSidebar"] * { color: #ede9fe !important; }

/* ── Hero header ── */
.hero {
    padding: 2.5rem 0 0;
    position: relative;
}
.hero-eyebrow {
    font-family: 'Outfit', sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    color: #7c3aed;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 700;
    color: #ede9fe;
    line-height: 1.1;
    margin: 0;
}
.hero-title em {
    font-style: italic;
    font-weight: 400;
    background: linear-gradient(135deg, #9d5fff 0%, #c4b5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    color: #6b5a8e;
    font-size: 0.9rem;
    margin-top: 0.5rem;
    font-weight: 300;
    letter-spacing: 0.01em;
}
.hero-rule {
    width: 48px;
    height: 2px;
    background: linear-gradient(90deg, #7c3aed, transparent);
    margin: 1.2rem 0;
}

/* ── Nav tabs ── */
.nav-wrap {
    display: flex;
    gap: 0;
    border-bottom: 1px solid #251b3e;
    margin-bottom: 2rem;
}
.nav-tab {
    font-family: 'Outfit', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    color: #6b5a8e;
    padding: 0.55rem 1.2rem 0.6rem;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
    transition: all 0.15s;
    letter-spacing: 0.02em;
}
.nav-tab:hover  { color: #c4b5fd; }
.nav-tab.active { color: #c4b5fd; border-bottom-color: #7c3aed; }

/* Override streamlit nav buttons */
div[data-testid="column"] .stButton > button {
    background: transparent !important;
    border: none !important;
    color: #6b5a8e !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    padding: 0.55rem 1.2rem 0.6rem !important;
    border-radius: 0 !important;
    border-bottom: 2px solid transparent !important;
    letter-spacing: 0.02em !important;
    width: 100% !important;
    transition: all 0.15s !important;
    box-shadow: none !important;
}
div[data-testid="column"] .stButton > button:hover {
    color: #c4b5fd !important;
    background: transparent !important;
    box-shadow: none !important;
}

/* ── Primary action button ── */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7c3aed 0%, #9d5fff 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    padding: 0.55rem 1.5rem !important;
    letter-spacing: 0.02em !important;
    transition: opacity 0.2s, box-shadow 0.2s !important;
    box-shadow: 0 4px 20px #7c3aed44 !important;
}
.stButton > button[kind="primary"]:hover {
    opacity: 0.88 !important;
    box-shadow: 0 4px 28px #7c3aed77 !important;
}

/* ── Cards ── */
.vault-card {
    background: #110e1c;
    border: 1px solid #251b3e;
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 0.8rem;
    position: relative;
    transition: border-color 0.2s, box-shadow 0.2s;
    overflow: hidden;
}
.vault-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(180deg, #7c3aed, transparent);
    opacity: 0;
    transition: opacity 0.2s;
}
.vault-card:hover { border-color: #7c3aed55; box-shadow: 0 8px 32px #7c3aed18; }
.vault-card:hover::before { opacity: 1; }

.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    font-weight: 700;
    color: #ede9fe;
    margin-bottom: 5px;
}
.card-desc {
    color: #9b8db5;
    font-size: 0.83rem;
    line-height: 1.65;
}

/* ── Tag pills ── */
.tag-subject {
    display: inline-block;
    background: #1e1040;
    color: #c4b5fd;
    border: 1px solid #3d2a7a;
    border-radius: 4px;
    padding: 2px 9px;
    font-size: 0.71rem;
    font-weight: 500;
    margin: 2px;
    letter-spacing: 0.02em;
}
.tag-skill {
    display: inline-block;
    background: #0f0a1f;
    color: #a78bfa;
    border: 1px solid #2d1f52;
    border-radius: 4px;
    padding: 2px 9px;
    font-size: 0.71rem;
    font-weight: 500;
    margin: 2px;
    letter-spacing: 0.02em;
}

/* Difficulty */
.tag-difficulty-Beginner     { background:#0a1f12; color:#6ee7b7; border:1px solid #1a4032; }
.tag-difficulty-Intermediate { background:#1a1000; color:#fcd34d; border:1px solid #3d2800; }
.tag-difficulty-Advanced     { background:#1a0820; color:#e879f9; border:1px solid #3d1050; }
.difficulty-badge {
    display: inline-block;
    border-radius: 6px;
    padding: 3px 11px;
    font-size: 0.71rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

/* ── Progress bar ── */
.bar-bg {
    background: #1e1640;
    border-radius: 3px;
    height: 4px;
    width: 100%;
    margin-top: 6px;
}
.bar-fill {
    background: linear-gradient(90deg, #7c3aed, #c4b5fd);
    border-radius: 3px;
    height: 4px;
}

/* ── Utility ── */
.section-label {
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    color: #6b5a8e;
    text-transform: uppercase;
    margin-bottom: 0.55rem;
}
.hint {
    color: #6b5a8e;
    font-size: 0.85rem;
    margin-bottom: 1.4rem;
    font-weight: 300;
    line-height: 1.7;
}
.empty-state {
    color: #4a3a6a;
    font-size: 0.9rem;
    margin-top: 3rem;
    text-align: center;
    font-style: italic;
}

/* Input */
.stTextInput > div > div > input {
    background: #110e1c !important;
    border: 1px solid #251b3e !important;
    border-radius: 10px !important;
    color: #ede9fe !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.9rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: #7c3aed !important;
    box-shadow: 0 0 0 2px #7c3aed33 !important;
}

/* File uploader */
[data-testid="stFileUploader"] {
    background: #110e1c !important;
    border: 1px dashed #251b3e !important;
    border-radius: 14px !important;
    transition: border-color 0.2s !important;
}
[data-testid="stFileUploader"]:hover {
    border-color: #7c3aed !important;
}

/* Expander */
details > summary {
    background: #110e1c !important;
    border: 1px solid #251b3e !important;
    border-radius: 12px !important;
    color: #ede9fe !important;
    font-family: 'Playfair Display', serif !important;
    padding: 0.8rem 1rem !important;
}
details[open] > summary { border-radius: 12px 12px 0 0 !important; }

hr { border-color: #1e1835 !important; }

.stSuccess { background: #0a1f12 !important; border-color: #1a4032 !important; color: #6ee7b7 !important; border-radius: 10px !important; }
.stAlert   { border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)


# ── Hero header ────────────────────────────────────────────────────────────────
st.markdown("""
<div class='hero'>
  <div class='hero-eyebrow'>✦ AI-Powered Library</div>
  <div class='hero-title'>Knowledge <em>Vault</em></div>
  <div class='hero-sub'>Upload once &mdash; find anything, instantly.</div>
  <div class='hero-rule'></div>
</div>
""", unsafe_allow_html=True)

# ── Inline nav buttons ─────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Upload"

pages = ["Upload", "Search", "Library", "Browse by Tag"]
nav_cols = st.columns([1.1, 1, 1, 1.4, 5])
for i, p in enumerate(pages):
    with nav_cols[i]:
        if st.button(p, key=f"nav_{p}"):
            st.session_state.page = p

page = st.session_state.page
st.markdown("<hr style='margin:0 0 1.8rem'>", unsafe_allow_html=True)

# Sidebar mirrors nav
with st.sidebar:
    st.markdown("<div style='font-family:Playfair Display,serif;font-size:1.25rem;color:#ede9fe;padding:0.5rem 0 0.25rem'>✦ Knowledge Vault</div>", unsafe_allow_html=True)
    st.markdown("---")
    sb = st.radio("", pages, index=pages.index(page), label_visibility="collapsed")
    if sb != page:
        st.session_state.page = sb
        st.rerun()
    st.markdown("---")
    st.markdown("<div style='color:#4a3a6a;font-size:0.78rem;line-height:1.8;font-style:italic'>Upload once.<br>Find anything.<br>AI does the rest.</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# UPLOAD
# ══════════════════════════════════════════════════════════════════════════════
if page == "Upload":
    st.markdown("<div class='hint'>Supports PDF, DOCX, and TXT. Drop in anything — lectures, articles, textbooks — and the AI builds the structure for you.</div>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("", type=["pdf", "docx", "txt"], label_visibility="collapsed")

    if uploaded_file:
        st.markdown(f"<div style='color:#9b8db5;font-size:0.82rem;margin:0.6rem 0 0.8rem'>📄 &nbsp;{uploaded_file.name}&nbsp; · &nbsp;{uploaded_file.size // 1024} KB</div>", unsafe_allow_html=True)

        if st.button("✦ Analyse & Add to Vault", type="primary"):
            from pipeline.ingest import ingest_document
            file_bytes = uploaded_file.read()
            try:
                with st.spinner("Analysing… this takes about 15 seconds"):
                    result = ingest_document(file_bytes, uploaded_file.name)

                st.success(f"✓ Added — {result.filename}")
                st.markdown("<br>", unsafe_allow_html=True)

                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown("<div class='section-label'>What this document covers</div>", unsafe_allow_html=True)
                    st.markdown(f"<div style='color:#9b8db5;line-height:1.75;font-size:0.88rem'>{result.description}</div>", unsafe_allow_html=True)
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
                            f"<div style='color:#4a3a6a;font-size:0.68rem;margin-top:3px'>{pct}% coverage</div>",
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
    st.markdown("<div class='hint'>Ask anything. The AI understands meaning, not just keywords — so \"how do transformers work\" finds your attention mechanism notes even if those words never appear.</div>", unsafe_allow_html=True)

    query = st.text_input("", placeholder="e.g.  how does backpropagation work")

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
            st.markdown(f"<div class='section-label' style='margin-bottom:1rem'>{len(results)} result{'s' if len(results)!=1 else ''} for &ldquo;{query}&rdquo;</div>", unsafe_allow_html=True)
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
                  <div style='margin-top:0.9rem'>
                    {"".join(f"<span class='tag-subject'>{s}</span>" for s in subj)}
                    {"".join(f"<span class='tag-skill'>{s}</span>" for s in skls[:5])}
                  </div>
                  <div style='margin-top:0.9rem'>
                    <div style='color:#4a3a6a;font-size:0.68rem;letter-spacing:0.08em'>RELEVANCE &nbsp; {sim}%</div>
                    <div class='bar-bg'><div class='bar-fill' style='width:{sim}%'></div></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# LIBRARY
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Library":
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
                    st.markdown(f"<div class='card-desc' style='margin-bottom:1rem'>{doc.get('description','No description.')}</div>", unsafe_allow_html=True)
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
    from db.supabase_client import get_all_tags, get_documents_by_tag
    try:
        all_tags = get_all_tags()
    except Exception as e:
        st.error(f"Could not load tags: {e}")
        all_tags = {"subject": [], "skill": []}

    cl, cr = st.columns([1, 2])
    with cl:
        st.markdown("<div class='section-label'>By subject</div>", unsafe_allow_html=True)
        sel_sub = st.radio("", ["(all)"] + all_tags["subject"], label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<div class='section-label'>By skill</div>", unsafe_allow_html=True)
        sel_skl = st.radio("", ["(all)"] + all_tags["skill"], label_visibility="collapsed")

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
                      <div style='margin-top:0.8rem'>
                        {"".join(f"<span class='tag-subject'>{s}</span>" for s in subj)}
                        {"".join(f"<span class='tag-skill'>{s}</span>" for s in skls)}
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown("<div class='empty-state'>Pick a subject or skill on the left.</div>", unsafe_allow_html=True)
