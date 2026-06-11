"""
app.py — Knowledge Vault
Run with: streamlit run app.py
"""

import streamlit as st

st.set_page_config(
    page_title="Knowledge Vault",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Outfit:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Outfit', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }

.stApp {
    background: linear-gradient(160deg, #1a0533 0%, #0f0221 50%, #1a0533 100%);
    min-height: 100vh;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #140328 !important;
    border-right: 1px solid #4a1f8a !important;
    width: 260px !important;
}
[data-testid="stSidebar"] > div { padding-top: 2rem; }

.sidebar-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 900;
    color: #f3e8ff;
    padding: 0 1rem 1.5rem;
    letter-spacing: -0.01em;
}
.sidebar-logo span {
    background: linear-gradient(135deg, #9333ea, #e879f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.sidebar-divider {
    height: 1px;
    background: linear-gradient(90deg, #4a1f8a, transparent);
    margin: 0 1rem 1.5rem;
}
.sidebar-section {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: #6d28d9;
    text-transform: uppercase;
    padding: 0 1.2rem 0.6rem;
}

/* Sidebar radio buttons */
[data-testid="stSidebar"] .stRadio > div {
    gap: 0.3rem;
}
[data-testid="stSidebar"] .stRadio label {
    background: transparent !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.7rem 1.2rem !important;
    color: #a78bfa !important;
    font-size: 0.95rem !important;
    font-weight: 500 !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    gap: 0.6rem !important;
    transition: background 0.15s, color 0.15s !important;
    width: 100% !important;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: #2d1057 !important;
    color: #f3e8ff !important;
}
[data-testid="stSidebar"] .stRadio label[data-checked="true"] {
    background: #2d1057 !important;
    color: #f3e8ff !important;
    border-left: 3px solid #9333ea !important;
}

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 3.5rem 0 1rem;
}
.hero-eyebrow {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.25em;
    color: #7c3aed;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 5.5rem;
    font-weight: 900;
    font-style: italic;
    color: #f3e8ff;
    line-height: 1.0;
    margin: 0 0 0.8rem;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #f3e8ff 0%, #c4b5fd 50%, #e879f9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    color: #a78bfa;
    font-size: 1.1rem;
    font-weight: 300;
    letter-spacing: 0.02em;
}

/* ── Intro ── */
.intro-box {
    background: linear-gradient(135deg, #2d1057 0%, #3b0f6e 100%);
    border: 1px solid #6d28d9;
    border-radius: 24px;
    padding: 2.2rem 2.8rem;
    margin: 2rem auto;
    max-width: 820px;
    position: relative;
    overflow: hidden;
}
.intro-box::before {
    content:'';
    position:absolute;
    top:-60px; right:-60px;
    width:200px; height:200px;
    background: radial-gradient(circle, #9333ea22, transparent 70%);
    border-radius:50%;
}
.intro-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 900;
    font-style: italic;
    color: #f3e8ff;
    margin-bottom: 0.8rem;
}
.intro-text {
    color: #c4b5fd;
    font-size: 0.97rem;
    line-height: 1.85;
    font-weight: 300;
}
.intro-steps {
    display: flex;
    gap: 1rem;
    margin-top: 1.8rem;
    flex-wrap: wrap;
}
.intro-step {
    flex: 1;
    min-width: 140px;
    background: #1a0533;
    border: 1px solid #4a1f8a;
    border-radius: 14px;
    padding: 1.1rem 1rem;
    text-align: center;
}
.intro-step-icon { font-size: 2rem; margin-bottom: 0.5rem; }
.intro-step-label { font-size: 0.82rem; font-weight: 600; color: #e9d5ff; letter-spacing: 0.03em; }
.intro-step-desc  { font-size: 0.75rem; color: #7c5cbf; margin-top: 0.25rem; font-weight: 300; }

/* ── Big upload button ── */
.upload-cta-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 2.5rem 0 1rem;
}
.upload-cta-label {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    color: #6d28d9;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

/* The big Upload button */
div[data-testid="stButton"] > button.upload-hero-btn,
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7c3aed 0%, #9333ea 50%, #a855f7 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 20px !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.3rem !important;
    padding: 1.2rem 3.5rem !important;
    letter-spacing: 0.04em !important;
    box-shadow: 0 8px 40px #9333ea66, 0 0 0 1px #a855f744 !important;
    transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s !important;
    width: auto !important;
    min-width: 260px !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-5px) scale(1.03) !important;
    box-shadow: 0 16px 56px #9333ea99, 0 0 0 2px #a855f766 !important;
}

/* Secondary buttons */
.stButton > button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid #4a1f8a !important;
    border-radius: 10px !important;
    color: #a78bfa !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    transition: all 0.15s !important;
    box-shadow: none !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color: #9333ea !important;
    color: #f3e8ff !important;
    background: #2d1057 !important;
    box-shadow: none !important;
}

/* ── Cards ── */
.vault-card {
    background: #230a42;
    border: 1px solid #4a1f8a;
    border-radius: 18px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s, border-color 0.2s;
}
.vault-card::before {
    content:'';
    position:absolute;
    top:0; left:0;
    width:4px; height:100%;
    background: linear-gradient(180deg, #9333ea, #e879f9);
    opacity:0;
    transition: opacity 0.2s;
}
.vault-card:hover { transform: translateY(-4px); border-color: #9333ea55; box-shadow: 0 12px 40px #9333ea22; }
.vault-card:hover::before { opacity: 1; }

.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    font-weight: 900;
    font-style: italic;
    color: #f3e8ff;
    margin-bottom: 6px;
}
.card-desc { color: #a78bfa; font-size: 0.88rem; line-height: 1.7; font-weight: 300; }

/* ── Tags ── */
.tag-subject {
    display: inline-block;
    background: #2d1057; color: #e9d5ff; border: 1px solid #6d28d9;
    border-radius: 6px; padding: 3px 11px; font-size: 0.75rem;
    font-weight: 500; margin: 3px; letter-spacing: 0.02em;
}
.tag-skill {
    display: inline-block;
    background: #1a0533; color: #c4b5fd; border: 1px solid #4a1f8a;
    border-radius: 6px; padding: 3px 11px; font-size: 0.75rem;
    font-weight: 500; margin: 3px; letter-spacing: 0.02em;
}
.tag-difficulty-Beginner     { background:#0a2015; color:#6ee7b7; border:1px solid #166534; }
.tag-difficulty-Intermediate { background:#1c1000; color:#fcd34d; border:1px solid #854d0e; }
.tag-difficulty-Advanced     { background:#200a33; color:#e879f9; border:1px solid #6d28d9; }
.difficulty-badge {
    display: inline-block; border-radius: 8px; padding: 4px 13px;
    font-size: 0.73rem; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase;
}

/* ── Bars ── */
.bar-bg { background:#2d1057; border-radius:4px; height:5px; width:100%; margin-top:6px; }
.bar-fill { background: linear-gradient(90deg, #7c3aed, #e879f9); border-radius:4px; height:5px; }

/* ── Util ── */
.section-label {
    font-size: 0.68rem; font-weight: 700; letter-spacing: 0.15em;
    color: #7c5cbf; text-transform: uppercase; margin-bottom: 0.6rem;
}
.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem; font-weight: 900; font-style: italic;
    color: #f3e8ff; margin-bottom: 0.6rem;
}
.hint { color: #a78bfa; font-size: 0.95rem; margin-bottom: 1.5rem; font-weight: 300; line-height: 1.8; }
.empty-state { color: #4a1f8a; font-size: 1rem; margin-top: 3rem; text-align: center; font-style: italic; }

.stTextInput > div > div > input {
    background: #230a42 !important; border: 1px solid #4a1f8a !important;
    border-radius: 12px !important; color: #f3e8ff !important;
    font-family: 'Outfit', sans-serif !important; font-size: 1rem !important;
    padding: 0.7rem 1rem !important;
}
.stTextInput > div > div > input:focus { border-color: #9333ea !important; box-shadow: 0 0 0 3px #9333ea33 !important; }
.stTextInput > div > div > input::placeholder { color: #7c5cbf !important; }

[data-testid="stFileUploader"] {
    background: #230a42 !important; border: 1px dashed #4a1f8a !important; border-radius: 16px !important;
}
[data-testid="stFileUploader"]:hover { border-color: #9333ea !important; }

details > summary {
    background: #230a42 !important; border: 1px solid #4a1f8a !important;
    border-radius: 14px !important; color: #f3e8ff !important;
    font-family: 'Playfair Display', serif !important; font-size: 1rem !important;
    font-weight: 900 !important; padding: 0.9rem 1.2rem !important;
}
details[open] > summary { border-radius: 14px 14px 0 0 !important; }
details > div {
    background: #1a0533 !important; border: 1px solid #4a1f8a !important;
    border-top: none !important; border-radius: 0 0 14px 14px !important; padding: 1rem 1.2rem !important;
}
hr { border-color: #2d1057 !important; }
.stSuccess { background:#0a2015 !important; border-color:#166534 !important; color:#6ee7b7 !important; border-radius:12px !important; }
.stAlert { border-radius: 12px !important; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<div class='sidebar-logo'>✦ Knowledge<br><span>Vault</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-section'>Navigate</div>", unsafe_allow_html=True)

    sidebar_pages = ["Home", "Search", "Library", "Browse by Tag"]
    sidebar_icons = ["🏠", "🔍", "📚", "🏷️"]
    options = [f"{icon}  {name}" for icon, name in zip(sidebar_icons, sidebar_pages)]

    current_idx = sidebar_pages.index(st.session_state.page) if st.session_state.page in sidebar_pages else 0
    choice = st.radio("nav", options, index=current_idx, label_visibility="collapsed")
    chosen_page = sidebar_pages[options.index(choice)]
    if chosen_page != st.session_state.page:
        st.session_state.page = chosen_page
        st.rerun()

    st.markdown("<br><div class='sidebar-divider'></div>", unsafe_allow_html=True)
    st.markdown("<div style='padding:0 1.2rem;color:#4a1f8a;font-size:0.8rem;line-height:1.9;font-style:italic'>Upload once.<br>Find anything.<br>AI does the rest.</div>", unsafe_allow_html=True)

page = st.session_state.page

# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":
    st.markdown("""
    <div class='hero'>
      <div class='hero-eyebrow'>✦ &nbsp; AI-Powered Document Library &nbsp; ✦</div>
      <div class='hero-title'>Knowledge Vault</div>
      <div class='hero-sub'>Your documents, intelligently organised.</div>
    </div>
    """, unsafe_allow_html=True)

    # Big centred upload button
    st.markdown("<div class='upload-cta-wrap'><div class='upload-cta-label'>Get started</div></div>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([2, 1.5, 2])
    with col_c:
        if st.button("✦  Upload a Document", type="primary", use_container_width=True):
            st.session_state.page = "Upload"
            st.rerun()

    # Intro
    st.markdown("""
    <div class='intro-box' style='margin-top:3rem'>
      <div class='intro-title'>How it works</div>
      <div class='intro-text'>
        Stop drowning in unsorted PDFs, lecture notes, and articles.
        Knowledge Vault reads every document you upload and automatically assigns
        <strong style='color:#e9d5ff'>subject tags</strong>,
        <strong style='color:#e9d5ff'>skill tags</strong>, and a
        <strong style='color:#e9d5ff'>difficulty level</strong> — no manual effort needed.
        When you want to learn something new, just search and the vault surfaces
        exactly which documents to read, ranked by relevance.
      </div>
      <div class='intro-steps'>
        <div class='intro-step'>
          <div class='intro-step-icon'>📤</div>
          <div class='intro-step-label'>Upload</div>
          <div class='intro-step-desc'>PDF, DOCX, or TXT</div>
        </div>
        <div class='intro-step'>
          <div class='intro-step-icon'>🤖</div>
          <div class='intro-step-label'>AI analyses</div>
          <div class='intro-step-desc'>Tags subjects, skills & level</div>
        </div>
        <div class='intro-step'>
          <div class='intro-step-icon'>🔍</div>
          <div class='intro-step-label'>Search</div>
          <div class='intro-step-desc'>Find by concept, not keyword</div>
        </div>
        <div class='intro-step'>
          <div class='intro-step-icon'>📚</div>
          <div class='intro-step-label'>Discover</div>
          <div class='intro-step-desc'>Know exactly what to read</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# UPLOAD (separate page reached from Home button or sidebar)
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Upload":
    st.markdown("<div class='page-title'>Upload a document</div>", unsafe_allow_html=True)
    st.markdown("<div class='hint'>Drop in a PDF, DOCX, or TXT — the AI will read it and automatically assign subjects, skills, and difficulty. No manual tagging needed.</div>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"], label_visibility="collapsed")

    if uploaded_file:
        st.markdown(f"<div style='color:#a78bfa;font-size:0.9rem;margin:0.6rem 0 0.9rem'>📄 &nbsp;{uploaded_file.name} &nbsp;·&nbsp; {uploaded_file.size // 1024} KB</div>", unsafe_allow_html=True)

        if st.button("✦  Analyse & Add to Vault", type="primary"):
            from pipeline.ingest import ingest_document
            file_bytes = uploaded_file.read()
            try:
                with st.spinner("Reading and analysing… (15–20 seconds)"):
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
    st.markdown("<div class='hint'>Describe what you want to learn. The AI finds relevant documents even without exact keyword matches.</div>", unsafe_allow_html=True)

    query = st.text_input("What topic or skill are you looking for?", placeholder="e.g.  gradient descent  ·  sorting algorithms  ·  probability distributions", label_visibility="collapsed")

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
