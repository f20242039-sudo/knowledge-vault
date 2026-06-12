"""
app.py — Knowledge Vault
Run with: streamlit run app.py
"""

import streamlit as st
from i18n import T, translate_tag, translate_difficulty

st.set_page_config(
    page_title="Knowledge Vault",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Outfit:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@300;400;500;600&family=Noto+Sans+Devanagari:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Outfit', 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }

.stApp {
    background: linear-gradient(160deg, #1a0533 0%, #0f0221 50%, #1a0533 100%);
    min-height: 100vh;
}

[data-testid="stSidebar"] {
    background: #140328 !important;
    border-right: 1px solid #4a1f8a !important;
    width: 260px !important;
}
[data-testid="stSidebar"] > div { padding-top: 2rem; }

.sidebar-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem; font-weight: 900; color: #f3e8ff;
    padding: 0 1rem 1.5rem; letter-spacing: -0.01em;
}
.sidebar-logo span {
    background: linear-gradient(135deg, #9333ea, #e879f9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.sidebar-divider {
    height: 1px; background: linear-gradient(90deg, #4a1f8a, transparent);
    margin: 0 1rem 1.5rem;
}
.sidebar-section {
    font-size: 0.62rem; font-weight: 700; letter-spacing: 0.18em;
    color: #6d28d9; text-transform: uppercase; padding: 0 1.2rem 0.6rem;
}

[data-testid="stSidebar"] .stRadio > div { gap: 0.3rem; }
[data-testid="stSidebar"] .stRadio label {
    background: transparent !important; border: none !important;
    border-radius: 10px !important; padding: 0.7rem 1.2rem !important;
    color: #a78bfa !important; font-size: 0.95rem !important; font-weight: 500 !important;
    cursor: pointer !important; display: flex !important; align-items: center !important;
    gap: 0.6rem !important; transition: background 0.15s, color 0.15s !important; width: 100% !important;
}
[data-testid="stSidebar"] .stRadio label:hover { background: #2d1057 !important; color: #f3e8ff !important; }
[data-testid="stSidebar"] .stRadio label[data-checked="true"] {
    background: #2d1057 !important; color: #f3e8ff !important; border-left: 3px solid #9333ea !important;
}

.hero { text-align: center; padding: 3.5rem 0 1rem; }
.hero-eyebrow { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.25em; color: #7c3aed; text-transform: uppercase; margin-bottom: 1.2rem; }
.hero-title {
    font-family: 'Playfair Display', serif; font-size: 5.5rem; font-weight: 900; font-style: italic;
    line-height: 1.0; margin: 0 0 0.8rem; letter-spacing: -0.02em;
    background: linear-gradient(135deg, #f3e8ff 0%, #c4b5fd 50%, #e879f9 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero-title-indic {
    font-family: 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif;
    font-size: 4rem; font-weight: 600; font-style: normal;
    line-height: 1.2; margin: 0 0 0.8rem;
    background: linear-gradient(135deg, #f3e8ff 0%, #c4b5fd 50%, #e879f9 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero-sub { color: #a78bfa; font-size: 1.1rem; font-weight: 300; letter-spacing: 0.02em; }

.intro-box {
    background: linear-gradient(135deg, #2d1057 0%, #3b0f6e 100%);
    border: 1px solid #6d28d9; border-radius: 24px; padding: 2.2rem 2.8rem;
    margin: 2rem auto; max-width: 820px; position: relative; overflow: hidden;
}
.intro-box::before {
    content:''; position:absolute; top:-60px; right:-60px;
    width:200px; height:200px;
    background: radial-gradient(circle, #9333ea22, transparent 70%); border-radius:50%;
}
.intro-title {
    font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 900;
    font-style: italic; color: #f3e8ff; margin-bottom: 0.8rem;
}
.intro-title-indic {
    font-family: 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif;
    font-size: 1.3rem; font-weight: 600; color: #f3e8ff; margin-bottom: 0.8rem;
}
.intro-text { color: #c4b5fd; font-size: 0.97rem; line-height: 1.85; font-weight: 300; }
.intro-steps { display: flex; gap: 1rem; margin-top: 1.8rem; flex-wrap: wrap; }
.intro-step {
    flex: 1; min-width: 140px; background: #1a0533; border: 1px solid #4a1f8a;
    border-radius: 14px; padding: 1.1rem 1rem; text-align: center;
}
.intro-step-icon { font-size: 2rem; margin-bottom: 0.5rem; }
.intro-step-label { font-size: 0.82rem; font-weight: 600; color: #e9d5ff; letter-spacing: 0.03em; }
.intro-step-desc  { font-size: 0.75rem; color: #7c5cbf; margin-top: 0.25rem; font-weight: 300; }

.upload-cta-wrap { display: flex; flex-direction: column; align-items: center; margin: 2.5rem 0 1rem; }
.upload-cta-label { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.2em; color: #6d28d9; text-transform: uppercase; margin-bottom: 1rem; }

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7c3aed 0%, #9333ea 50%, #a855f7 100%) !important;
    color: #fff !important; border: none !important; border-radius: 20px !important;
    font-family: 'Outfit', 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif !important;
    font-weight: 700 !important; font-size: 1.3rem !important; padding: 1.2rem 3.5rem !important;
    letter-spacing: 0.04em !important;
    box-shadow: 0 8px 40px #9333ea66, 0 0 0 1px #a855f744 !important;
    transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s !important;
    width: auto !important; min-width: 260px !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-5px) scale(1.03) !important;
    box-shadow: 0 16px 56px #9333ea99, 0 0 0 2px #a855f766 !important;
}
.stButton > button[kind="secondary"] {
    background: transparent !important; border: 1px solid #4a1f8a !important;
    border-radius: 10px !important; color: #a78bfa !important;
    font-family: 'Outfit', 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif !important;
    font-size: 0.85rem !important; font-weight: 500 !important;
    transition: all 0.15s !important; box-shadow: none !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color: #9333ea !important; color: #f3e8ff !important;
    background: #2d1057 !important; box-shadow: none !important;
}

.vault-card {
    background: #230a42; border: 1px solid #4a1f8a; border-radius: 18px;
    padding: 1.5rem 1.8rem; margin-bottom: 1rem; position: relative; overflow: hidden;
    transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s, border-color 0.2s;
}
.vault-card::before {
    content:''; position:absolute; top:0; left:0; width:4px; height:100%;
    background: linear-gradient(180deg, #9333ea, #e879f9); opacity:0; transition: opacity 0.2s;
}
.vault-card:hover { transform: translateY(-4px); border-color: #9333ea55; box-shadow: 0 12px 40px #9333ea22; }
.vault-card:hover::before { opacity: 1; }

.card-title { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 900; font-style: italic; color: #f3e8ff; margin-bottom: 6px; }
.card-desc  { color: #a78bfa; font-size: 0.88rem; line-height: 1.7; font-weight: 300; }

.tag-subject {
    display: inline-block; background: #2d1057; color: #e9d5ff; border: 1px solid #6d28d9;
    border-radius: 6px; padding: 3px 11px; font-size: 0.75rem; font-weight: 500; margin: 3px; letter-spacing: 0.02em;
}
.tag-skill {
    display: inline-block; background: #1a0533; color: #c4b5fd; border: 1px solid #4a1f8a;
    border-radius: 6px; padding: 3px 11px; font-size: 0.75rem; font-weight: 500; margin: 3px; letter-spacing: 0.02em;
}
.tag-difficulty-Beginner     { background:#0a2015; color:#6ee7b7; border:1px solid #166534; }
.tag-difficulty-Intermediate { background:#1c1000; color:#fcd34d; border:1px solid #854d0e; }
.tag-difficulty-Advanced     { background:#200a33; color:#e879f9; border:1px solid #6d28d9; }
.difficulty-badge { display:inline-block; border-radius:8px; padding:4px 13px; font-size:0.73rem; font-weight:700; letter-spacing:0.05em; text-transform:uppercase; }

.bar-bg  { background:#2d1057; border-radius:4px; height:5px; width:100%; margin-top:6px; }
.bar-fill{ background: linear-gradient(90deg, #7c3aed, #e879f9); border-radius:4px; height:5px; }

.section-label { font-size:0.68rem; font-weight:700; letter-spacing:0.15em; color:#7c5cbf; text-transform:uppercase; margin-bottom:0.6rem; }
.page-title { font-family:'Playfair Display',serif; font-size:2.4rem; font-weight:900; font-style:italic; color:#f3e8ff; margin-bottom:0.6rem; }
.page-title-indic { font-family:'Noto Sans Telugu','Noto Sans Devanagari',sans-serif; font-size:2rem; font-weight:600; color:#f3e8ff; margin-bottom:0.6rem; }
.hint { color:#a78bfa; font-size:0.95rem; margin-bottom:1.5rem; font-weight:300; line-height:1.8; }
.empty-state { color:#4a1f8a; font-size:1rem; margin-top:3rem; text-align:center; font-style:italic; }

.stTextInput > div > div > input {
    background:#230a42 !important; border:1px solid #4a1f8a !important; border-radius:12px !important;
    color:#f3e8ff !important; font-family:'Outfit','Noto Sans Telugu','Noto Sans Devanagari',sans-serif !important;
    font-size:1rem !important; padding:0.7rem 1rem !important;
}
.stTextInput > div > div > input:focus { border-color:#9333ea !important; box-shadow:0 0 0 3px #9333ea33 !important; }
.stTextInput > div > div > input::placeholder { color:#7c5cbf !important; }

[data-testid="stFileUploader"] { background:#230a42 !important; border:1px dashed #4a1f8a !important; border-radius:16px !important; }
[data-testid="stFileUploader"]:hover { border-color:#9333ea !important; }

details > summary {
    background:#230a42 !important; border:1px solid #4a1f8a !important; border-radius:14px !important;
    color:#f3e8ff !important; font-family:'Playfair Display',serif !important; font-size:1rem !important;
    font-weight:900 !important; padding:0.9rem 1.2rem !important;
}
details[open] > summary { border-radius:14px 14px 0 0 !important; }
details > div {
    background:#1a0533 !important; border:1px solid #4a1f8a !important; border-top:none !important;
    border-radius:0 0 14px 14px !important; padding:1rem 1.2rem !important;
}
hr { border-color:#2d1057 !important; }
.stSuccess { background:#0a2015 !important; border-color:#166534 !important; color:#6ee7b7 !important; border-radius:12px !important; }
.stAlert   { border-radius:12px !important; }
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "lang" not in st.session_state:
    st.session_state.lang = "en"

lang = st.session_state.lang
is_indic = lang in ("te", "hi")

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<div class='sidebar-logo'>✦ Knowledge<br><span>Vault</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ── Language toggle ────────────────────────────────────────────────────────
    st.markdown(f"<div class='sidebar-section'>{T('lang_label')}</div>", unsafe_allow_html=True)
    lang_choice = st.radio(
        "lang_radio",
        ["🇬🇧  English", "🇮🇳  తెలుగు", "🇮🇳  हिंदी"],
        index={"en": 0, "te": 1, "hi": 2}.get(lang, 0),
        label_visibility="collapsed",
        key="lang_radio",
    )
    new_lang = {"🇬🇧  English": "en", "🇮🇳  తెలుగు": "te", "🇮🇳  हिंदी": "hi"}[lang_choice]
    if new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
        st.rerun()

    st.markdown("<br><div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ── Navigation ─────────────────────────────────────────────────────────────
    st.markdown(f"<div class='sidebar-section'>{T('nav_label')}</div>", unsafe_allow_html=True)

    sidebar_pages = ["Home", "Upload", "Search", "Library", "Browse by Tag"]
    nav_labels = [T("nav_home"), T("nav_upload"), T("nav_search"), T("nav_library"), T("nav_browse")]

    current_idx = sidebar_pages.index(st.session_state.page) if st.session_state.page in sidebar_pages else 0
    choice = st.radio("nav", nav_labels, index=current_idx, label_visibility="collapsed")
    chosen_page = sidebar_pages[nav_labels.index(choice)]
    if chosen_page != st.session_state.page:
        st.session_state.page = chosen_page
        st.rerun()

    # ── AI Provider ────────────────────────────────────────────────────────────
    st.markdown("<br><div class='sidebar-divider'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sidebar-section'>{T('ai_provider')}</div>", unsafe_allow_html=True)

    provider = st.radio(
        "provider_select",
        ["☁️  Groq (Cloud)", "🖥️  Ollama (Local)"],
        index=0 if st.session_state.get("ai_provider", "groq") == "groq" else 1,
        label_visibility="collapsed",
        key="provider_radio",
    )
    is_groq = provider.startswith("☁️")
    st.session_state.ai_provider = "groq" if is_groq else "ollama"

    if is_groq:
        import os
        env_key = os.getenv("GROQ_API_KEY", "")
        groq_key = st.text_input(
            "Groq API Key",
            value=st.session_state.get("groq_api_key", env_key),
            type="password",
            placeholder="gsk_…",
            help="Your key is only stored in session memory.",
        )
        st.session_state.groq_api_key = groq_key
        groq_model = st.text_input(
            "Model",
            value=st.session_state.get("groq_model", "llama-3.3-70b-versatile"),
            placeholder="llama-3.3-70b-versatile",
        )
        st.session_state.groq_model = groq_model
        if groq_key:
            st.markdown(f"<div style='color:#6ee7b7;font-size:0.75rem;margin-top:0.3rem'>{T('key_set')}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='color:#f87171;font-size:0.75rem;margin-top:0.3rem'>{T('no_key')}</div>", unsafe_allow_html=True)
    else:
        ollama_url = st.text_input(
            "Ollama base URL",
            value=st.session_state.get("ollama_url", "http://localhost:11434"),
            placeholder="http://localhost:11434",
        )
        st.session_state.ollama_url = ollama_url
        ollama_model = st.text_input(
            "Model",
            value=st.session_state.get("ollama_model", "llama3.2"),
            placeholder="llama3.2",
        )
        st.session_state.ollama_model = ollama_model
        st.markdown(
            f"<div style='padding:0 0.2rem;color:#7c5cbf;font-size:0.75rem;margin-top:0.4rem;line-height:1.7'>"
            f"{T('ollama_hint')}<br>"
            f"<code style='font-size:0.7rem;color:#9333ea'>ollama pull llama3.2</code></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<br><div class='sidebar-divider'></div>", unsafe_allow_html=True)
    tagline = T("tagline").replace("\n", "<br>")
    st.markdown(f"<div style='padding:0 1.2rem;color:#4a1f8a;font-size:0.8rem;line-height:1.9;font-style:italic'>{tagline}</div>", unsafe_allow_html=True)

    st.markdown("<br><div class='sidebar-divider'></div><br>", unsafe_allow_html=True)
    review_url = "https://docs.google.com/forms/d/e/1FAIpQLSd0vCbRpt_d0VluB1axjA4skCcmr-TA3eJ1A0RdWxt8PTYB1Q/viewform?usp=publish-editor"
    st.markdown(
        f"""<a href='{review_url}' target='_blank' style='display:block;margin:0 1rem;padding:0.65rem 1rem;background:linear-gradient(135deg,#7c3aed,#9333ea);color:#fff;font-family:Outfit,sans-serif;font-size:0.85rem;font-weight:600;text-align:center;text-decoration:none;border-radius:12px;letter-spacing:0.03em;box-shadow:0 4px 20px #9333ea55'>✦ &nbsp; Give a Review!</a>""",
        unsafe_allow_html=True
    )
Run with: streamlit run app.py
"""

import streamlit as st
from i18n import T, translate_tag, translate_difficulty

st.set_page_config(
    page_title="Knowledge Vault",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,900;1,900&family=Outfit:wght@300;400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@300;400;500;600&family=Noto+Sans+Devanagari:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Outfit', 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }

.stApp {
    background: linear-gradient(160deg, #1a0533 0%, #0f0221 50%, #1a0533 100%);
    min-height: 100vh;
}

[data-testid="stSidebar"] {
    background: #140328 !important;
    border-right: 1px solid #4a1f8a !important;
    width: 260px !important;
}
[data-testid="stSidebar"] > div { padding-top: 2rem; }

.sidebar-logo {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem; font-weight: 900; color: #f3e8ff;
    padding: 0 1rem 1.5rem; letter-spacing: -0.01em;
}
.sidebar-logo span {
    background: linear-gradient(135deg, #9333ea, #e879f9);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.sidebar-divider {
    height: 1px; background: linear-gradient(90deg, #4a1f8a, transparent);
    margin: 0 1rem 1.5rem;
}
.sidebar-section {
    font-size: 0.62rem; font-weight: 700; letter-spacing: 0.18em;
    color: #6d28d9; text-transform: uppercase; padding: 0 1.2rem 0.6rem;
}

[data-testid="stSidebar"] .stRadio > div { gap: 0.3rem; }
[data-testid="stSidebar"] .stRadio label {
    background: transparent !important; border: none !important;
    border-radius: 10px !important; padding: 0.7rem 1.2rem !important;
    color: #a78bfa !important; font-size: 0.95rem !important; font-weight: 500 !important;
    cursor: pointer !important; display: flex !important; align-items: center !important;
    gap: 0.6rem !important; transition: background 0.15s, color 0.15s !important; width: 100% !important;
}
[data-testid="stSidebar"] .stRadio label:hover { background: #2d1057 !important; color: #f3e8ff !important; }
[data-testid="stSidebar"] .stRadio label[data-checked="true"] {
    background: #2d1057 !important; color: #f3e8ff !important; border-left: 3px solid #9333ea !important;
}

.hero { text-align: center; padding: 3.5rem 0 1rem; }
.hero-eyebrow { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.25em; color: #7c3aed; text-transform: uppercase; margin-bottom: 1.2rem; }
.hero-title {
    font-family: 'Playfair Display', serif; font-size: 5.5rem; font-weight: 900; font-style: italic;
    line-height: 1.0; margin: 0 0 0.8rem; letter-spacing: -0.02em;
    background: linear-gradient(135deg, #f3e8ff 0%, #c4b5fd 50%, #e879f9 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero-title-indic {
    font-family: 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif;
    font-size: 4rem; font-weight: 600; font-style: normal;
    line-height: 1.2; margin: 0 0 0.8rem;
    background: linear-gradient(135deg, #f3e8ff 0%, #c4b5fd 50%, #e879f9 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero-sub { color: #a78bfa; font-size: 1.1rem; font-weight: 300; letter-spacing: 0.02em; }

.intro-box {
    background: linear-gradient(135deg, #2d1057 0%, #3b0f6e 100%);
    border: 1px solid #6d28d9; border-radius: 24px; padding: 2.2rem 2.8rem;
    margin: 2rem auto; max-width: 820px; position: relative; overflow: hidden;
}
.intro-box::before {
    content:''; position:absolute; top:-60px; right:-60px;
    width:200px; height:200px;
    background: radial-gradient(circle, #9333ea22, transparent 70%); border-radius:50%;
}
.intro-title {
    font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 900;
    font-style: italic; color: #f3e8ff; margin-bottom: 0.8rem;
}
.intro-title-indic {
    font-family: 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif;
    font-size: 1.3rem; font-weight: 600; color: #f3e8ff; margin-bottom: 0.8rem;
}
.intro-text { color: #c4b5fd; font-size: 0.97rem; line-height: 1.85; font-weight: 300; }
.intro-steps { display: flex; gap: 1rem; margin-top: 1.8rem; flex-wrap: wrap; }
.intro-step {
    flex: 1; min-width: 140px; background: #1a0533; border: 1px solid #4a1f8a;
    border-radius: 14px; padding: 1.1rem 1rem; text-align: center;
}
.intro-step-icon { font-size: 2rem; margin-bottom: 0.5rem; }
.intro-step-label { font-size: 0.82rem; font-weight: 600; color: #e9d5ff; letter-spacing: 0.03em; }
.intro-step-desc  { font-size: 0.75rem; color: #7c5cbf; margin-top: 0.25rem; font-weight: 300; }

.upload-cta-wrap { display: flex; flex-direction: column; align-items: center; margin: 2.5rem 0 1rem; }
.upload-cta-label { font-size: 0.72rem; font-weight: 700; letter-spacing: 0.2em; color: #6d28d9; text-transform: uppercase; margin-bottom: 1rem; }

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #7c3aed 0%, #9333ea 50%, #a855f7 100%) !important;
    color: #fff !important; border: none !important; border-radius: 20px !important;
    font-family: 'Outfit', 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif !important;
    font-weight: 700 !important; font-size: 1.3rem !important; padding: 1.2rem 3.5rem !important;
    letter-spacing: 0.04em !important;
    box-shadow: 0 8px 40px #9333ea66, 0 0 0 1px #a855f744 !important;
    transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s !important;
    width: auto !important; min-width: 260px !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-5px) scale(1.03) !important;
    box-shadow: 0 16px 56px #9333ea99, 0 0 0 2px #a855f766 !important;
}
.stButton > button[kind="secondary"] {
    background: transparent !important; border: 1px solid #4a1f8a !important;
    border-radius: 10px !important; color: #a78bfa !important;
    font-family: 'Outfit', 'Noto Sans Telugu', 'Noto Sans Devanagari', sans-serif !important;
    font-size: 0.85rem !important; font-weight: 500 !important;
    transition: all 0.15s !important; box-shadow: none !important;
}
.stButton > button[kind="secondary"]:hover {
    border-color: #9333ea !important; color: #f3e8ff !important;
    background: #2d1057 !important; box-shadow: none !important;
}

.vault-card {
    background: #230a42; border: 1px solid #4a1f8a; border-radius: 18px;
    padding: 1.5rem 1.8rem; margin-bottom: 1rem; position: relative; overflow: hidden;
    transition: transform 0.2s cubic-bezier(.34,1.56,.64,1), box-shadow 0.2s, border-color 0.2s;
}
.vault-card::before {
    content:''; position:absolute; top:0; left:0; width:4px; height:100%;
    background: linear-gradient(180deg, #9333ea, #e879f9); opacity:0; transition: opacity 0.2s;
}
.vault-card:hover { transform: translateY(-4px); border-color: #9333ea55; box-shadow: 0 12px 40px #9333ea22; }
.vault-card:hover::before { opacity: 1; }

.card-title { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 900; font-style: italic; color: #f3e8ff; margin-bottom: 6px; }
.card-desc  { color: #a78bfa; font-size: 0.88rem; line-height: 1.7; font-weight: 300; }

.tag-subject {
    display: inline-block; background: #2d1057; color: #e9d5ff; border: 1px solid #6d28d9;
    border-radius: 6px; padding: 3px 11px; font-size: 0.75rem; font-weight: 500; margin: 3px; letter-spacing: 0.02em;
}
.tag-skill {
    display: inline-block; background: #1a0533; color: #c4b5fd; border: 1px solid #4a1f8a;
    border-radius: 6px; padding: 3px 11px; font-size: 0.75rem; font-weight: 500; margin: 3px; letter-spacing: 0.02em;
}
.tag-difficulty-Beginner     { background:#0a2015; color:#6ee7b7; border:1px solid #166534; }
.tag-difficulty-Intermediate { background:#1c1000; color:#fcd34d; border:1px solid #854d0e; }
.tag-difficulty-Advanced     { background:#200a33; color:#e879f9; border:1px solid #6d28d9; }
.difficulty-badge { display:inline-block; border-radius:8px; padding:4px 13px; font-size:0.73rem; font-weight:700; letter-spacing:0.05em; text-transform:uppercase; }

.bar-bg  { background:#2d1057; border-radius:4px; height:5px; width:100%; margin-top:6px; }
.bar-fill{ background: linear-gradient(90deg, #7c3aed, #e879f9); border-radius:4px; height:5px; }

.section-label { font-size:0.68rem; font-weight:700; letter-spacing:0.15em; color:#7c5cbf; text-transform:uppercase; margin-bottom:0.6rem; }
.page-title { font-family:'Playfair Display',serif; font-size:2.4rem; font-weight:900; font-style:italic; color:#f3e8ff; margin-bottom:0.6rem; }
.page-title-indic { font-family:'Noto Sans Telugu','Noto Sans Devanagari',sans-serif; font-size:2rem; font-weight:600; color:#f3e8ff; margin-bottom:0.6rem; }
.hint { color:#a78bfa; font-size:0.95rem; margin-bottom:1.5rem; font-weight:300; line-height:1.8; }
.empty-state { color:#4a1f8a; font-size:1rem; margin-top:3rem; text-align:center; font-style:italic; }

.stTextInput > div > div > input {
    background:#230a42 !important; border:1px solid #4a1f8a !important; border-radius:12px !important;
    color:#f3e8ff !important; font-family:'Outfit','Noto Sans Telugu','Noto Sans Devanagari',sans-serif !important;
    font-size:1rem !important; padding:0.7rem 1rem !important;
}
.stTextInput > div > div > input:focus { border-color:#9333ea !important; box-shadow:0 0 0 3px #9333ea33 !important; }
.stTextInput > div > div > input::placeholder { color:#7c5cbf !important; }

[data-testid="stFileUploader"] { background:#230a42 !important; border:1px dashed #4a1f8a !important; border-radius:16px !important; }
[data-testid="stFileUploader"]:hover { border-color:#9333ea !important; }

details > summary {
    background:#230a42 !important; border:1px solid #4a1f8a !important; border-radius:14px !important;
    color:#f3e8ff !important; font-family:'Playfair Display',serif !important; font-size:1rem !important;
    font-weight:900 !important; padding:0.9rem 1.2rem !important;
}
details[open] > summary { border-radius:14px 14px 0 0 !important; }
details > div {
    background:#1a0533 !important; border:1px solid #4a1f8a !important; border-top:none !important;
    border-radius:0 0 14px 14px !important; padding:1rem 1.2rem !important;
}
hr { border-color:#2d1057 !important; }
.stSuccess { background:#0a2015 !important; border-color:#166534 !important; color:#6ee7b7 !important; border-radius:12px !important; }
.stAlert   { border-radius:12px !important; }
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "lang" not in st.session_state:
    st.session_state.lang = "en"

lang = st.session_state.lang
is_indic = lang in ("te", "hi")

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<div class='sidebar-logo'>✦ Knowledge<br><span>Vault</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ── Language toggle ────────────────────────────────────────────────────────
    st.markdown(f"<div class='sidebar-section'>{T('lang_label')}</div>", unsafe_allow_html=True)
    lang_choice = st.radio(
        "lang_radio",
        ["🇬🇧  English", "🇮🇳  తెలుగు", "🇮🇳  हिंदी"],
        index={"en": 0, "te": 1, "hi": 2}.get(lang, 0),
        label_visibility="collapsed",
        key="lang_radio",
    )
    new_lang = {"🇬🇧  English": "en", "🇮🇳  తెలుగు": "te", "🇮🇳  हिंदी": "hi"}[lang_choice]
    if new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
        st.rerun()

    st.markdown("<br><div class='sidebar-divider'></div>", unsafe_allow_html=True)

    # ── Navigation ─────────────────────────────────────────────────────────────
    st.markdown(f"<div class='sidebar-section'>{T('nav_label')}</div>", unsafe_allow_html=True)

    sidebar_pages = ["Home", "Upload", "Search", "Library", "Browse by Tag"]
    nav_labels = [T("nav_home"), T("nav_upload"), T("nav_search"), T("nav_library"), T("nav_browse")]

    current_idx = sidebar_pages.index(st.session_state.page) if st.session_state.page in sidebar_pages else 0
    choice = st.radio("nav", nav_labels, index=current_idx, label_visibility="collapsed")
    chosen_page = sidebar_pages[nav_labels.index(choice)]
    if chosen_page != st.session_state.page:
        st.session_state.page = chosen_page
        st.rerun()

    # ── AI Provider ────────────────────────────────────────────────────────────
    st.markdown("<br><div class='sidebar-divider'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sidebar-section'>{T('ai_provider')}</div>", unsafe_allow_html=True)

    provider = st.radio(
        "provider_select",
        ["☁️  Groq (Cloud)", "🖥️  Ollama (Local)"],
        index=0 if st.session_state.get("ai_provider", "groq") == "groq" else 1,
        label_visibility="collapsed",
        key="provider_radio",
    )
    is_groq = provider.startswith("☁️")
    st.session_state.ai_provider = "groq" if is_groq else "ollama"

    if is_groq:
        import os
        env_key = os.getenv("GROQ_API_KEY", "")
        groq_key = st.text_input(
            "Groq API Key",
            value=st.session_state.get("groq_api_key", env_key),
            type="password",
            placeholder="gsk_…",
            help="Your key is only stored in session memory.",
        )
        st.session_state.groq_api_key = groq_key
        groq_model = st.text_input(
            "Model",
            value=st.session_state.get("groq_model", "llama-3.3-70b-versatile"),
            placeholder="llama-3.3-70b-versatile",
        )
        st.session_state.groq_model = groq_model
        if groq_key:
            st.markdown(f"<div style='color:#6ee7b7;font-size:0.75rem;margin-top:0.3rem'>{T('key_set')}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='color:#f87171;font-size:0.75rem;margin-top:0.3rem'>{T('no_key')}</div>", unsafe_allow_html=True)
    else:
        ollama_url = st.text_input(
            "Ollama base URL",
            value=st.session_state.get("ollama_url", "http://localhost:11434"),
            placeholder="http://localhost:11434",
        )
        st.session_state.ollama_url = ollama_url
        ollama_model = st.text_input(
            "Model",
            value=st.session_state.get("ollama_model", "llama3.2"),
            placeholder="llama3.2",
        )
        st.session_state.ollama_model = ollama_model
        st.markdown(
            f"<div style='padding:0 0.2rem;color:#7c5cbf;font-size:0.75rem;margin-top:0.4rem;line-height:1.7'>"
            f"{T('ollama_hint')}<br>"
            f"<code style='font-size:0.7rem;color:#9333ea'>ollama pull llama3.2</code></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<br><div class='sidebar-divider'></div>", unsafe_allow_html=True)
    tagline = T("tagline").replace("\n", "<br>")
    st.markdown(f"<div style='padding:0 1.2rem;color:#4a1f8a;font-size:0.8rem;line-height:1.9;font-style:italic'>{tagline}</div>", unsafe_allow_html=True)

    st.markdown("<br><div class='sidebar-divider'></div><br>", unsafe_allow_html=True)
    st.markdown("""
    <a href='https://docs.google.com/forms/d/e/1FAIpQLSd0vCbRpt_d0VluB1axjA4skCcmr-TA3eJ1A0RdWxt8PTYB1Q/viewform?usp=publish-editor'
       target='_blank'
       style='
         display: block;
         margin: 0 1rem;
         padding: 0.65rem 1rem;
         background: linear-gradient(135deg, #7c3aed, #9333ea);
         color: #fff !important;
         font-family: Outfit, sans-serif;
         font-size: 0.85rem;
         font-weight: 600;
         text-align: center;
         text-decoration: none;
         border-radius: 12px;
         letter-spacing: 0.03em;
         box-shadow: 0 4px 20px #9333ea55;
       '
    >
      ✦ &nbsp; Give a Review!
    </a>
    """, unsafe_allow_html=True)


def _get_provider_cfg() -> dict:
    if st.session_state.get("ai_provider", "groq") == "groq":
        import os
        return {
            "provider": "groq",
            "api_key":  st.session_state.get("groq_api_key", os.getenv("GROQ_API_KEY", "")),
            "model":    st.session_state.get("groq_model", "llama-3.3-70b-versatile"),
        }
    else:
        return {
            "provider": "ollama",
            "base_url": st.session_state.get("ollama_url", "http://localhost:11434"),
            "model":    st.session_state.get("ollama_model", "llama3.2"),
        }


def page_title(key: str):
    """Render page title using correct font class for current language."""
    cls = "page-title-indic" if is_indic else "page-title"
    st.markdown(f"<div class='{cls}'>{T(key)}</div>", unsafe_allow_html=True)


page = st.session_state.page

# ══════════════════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "Home":
    title_cls = "hero-title-indic" if is_indic else "hero-title"
    intro_title_cls = "intro-title-indic" if is_indic else "intro-title"

    st.markdown(f"""
    <div class='hero'>
      <div class='hero-eyebrow'>{T('hero_eyebrow')}</div>
      <div class='{title_cls}'>{T('hero_title')}</div>
      <div class='hero-sub'>{T('hero_sub')}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<div class='upload-cta-wrap'><div class='upload-cta-label'>{T('get_started')}</div></div>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([2, 1.5, 2])
    with col_c:
        if st.button(T("upload_btn"), type="primary", use_container_width=True):
            st.session_state.page = "Upload"
            st.rerun()

    st.markdown(f"""
    <div class='intro-box' style='margin-top:3rem'>
      <div class='{intro_title_cls}'>{T('how_it_works')}</div>
      <div class='intro-text'>{T('intro_text')}</div>
      <div class='intro-steps'>
        <div class='intro-step'>
          <div class='intro-step-icon'>📤</div>
          <div class='intro-step-label'>{T('step_upload')}</div>
          <div class='intro-step-desc'>{T('step_upload_desc')}</div>
        </div>
        <div class='intro-step'>
          <div class='intro-step-icon'>🤖</div>
          <div class='intro-step-label'>{T('step_ai')}</div>
          <div class='intro-step-desc'>{T('step_ai_desc')}</div>
        </div>
        <div class='intro-step'>
          <div class='intro-step-icon'>🔍</div>
          <div class='intro-step-label'>{T('step_search')}</div>
          <div class='intro-step-desc'>{T('step_search_desc')}</div>
        </div>
        <div class='intro-step'>
          <div class='intro-step-icon'>📚</div>
          <div class='intro-step-label'>{T('step_discover')}</div>
          <div class='intro-step-desc'>{T('step_discover_desc')}</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# UPLOAD
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Upload":
    page_title("upload_title")
    st.markdown(f"<div class='hint'>{T('upload_hint')}</div>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"], label_visibility="collapsed")

    if uploaded_file:
        st.markdown(f"<div style='color:#a78bfa;font-size:0.9rem;margin:0.6rem 0 0.9rem'>📄 &nbsp;{uploaded_file.name} &nbsp;·&nbsp; {uploaded_file.size // 1024} KB</div>", unsafe_allow_html=True)

        if st.button(T("analyse_btn"), type="primary"):
            from pipeline.ingest import ingest_document
            file_bytes = uploaded_file.read()
            provider_cfg = _get_provider_cfg()
            provider_label = "Groq" if provider_cfg["provider"] == "groq" else f"Ollama ({provider_cfg['model']})"
            try:
                with st.spinner(f"{T('analysing')} ({provider_label})… (15–20s)"):
                    result = ingest_document(file_bytes, uploaded_file.name, provider_cfg=provider_cfg)

                st.success(f"{T('added_ok')} — {result.filename}")
                st.markdown("<br>", unsafe_allow_html=True)

                col1, col2 = st.columns([3, 1])
                with col1:
                    st.markdown(f"<div class='section-label'>{T('what_covers')}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div style='color:#a78bfa;line-height:1.8;font-size:0.95rem;font-weight:300'>{result.description}</div>", unsafe_allow_html=True)
                with col2:
                    diff_en = result.difficulty
                    diff_display = translate_difficulty(diff_en)
                    diff_cls = f"tag-difficulty-{diff_en}"
                    st.markdown(f"<div class='section-label'>{T('level_label')}</div><span class='difficulty-badge {diff_cls}'>{diff_display}</span>", unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"<div class='section-label'>{T('subjects_label')}</div>", unsafe_allow_html=True)
                st.markdown(" ".join(f"<span class='tag-subject'>{translate_tag(s)}</span>" for s in result.subjects), unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"<div class='section-label'>{T('skills_label')}</div>", unsafe_allow_html=True)
                for skill in sorted(result.skills, key=lambda x: x["coverage"], reverse=True):
                    c1, c2 = st.columns([2, 3])
                    with c1:
                        st.markdown(f"<span class='tag-skill'>{translate_tag(skill['name'])}</span>", unsafe_allow_html=True)
                    with c2:
                        pct = skill["coverage"]
                        st.markdown(
                            f"<div class='bar-bg'><div class='bar-fill' style='width:{pct}%'></div></div>"
                            f"<div style='color:#6d28d9;font-size:0.7rem;margin-top:3px'>{pct}% {T('coverage_label')}</div>",
                            unsafe_allow_html=True,
                        )
            except ValueError as e:
                st.error(f"{T('err_process')} {e}")
            except Exception as e:
                st.error(f"{T('err_generic')} {e}")

# ══════════════════════════════════════════════════════════════════════════════
# SEARCH
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Search":
    page_title("search_title")
    st.markdown(f"<div class='hint'>{T('search_hint')}</div>", unsafe_allow_html=True)

    query = st.text_input("search_input", placeholder=T("search_placeholder"), label_visibility="collapsed")

    if query:
        from ai.embedder import embed
        from db.supabase_client import search_documents
        with st.spinner(T("searching")):
            try:
                results = search_documents(embed(query), limit=10)
            except Exception as e:
                st.error(f"{T('search_fail')} {e}")
                results = []

        if not results:
            st.markdown(f"<div class='empty-state'>{T('no_results')}</div>", unsafe_allow_html=True)
        else:
            count = len(results)
            result_word = T("result_singular") if count == 1 else T("results_for")
            st.markdown(f"<div class='section-label' style='margin-bottom:1.2rem'>{count} {result_word} &ldquo;{query}&rdquo;</div>", unsafe_allow_html=True)

            for doc in results:
                sim  = int(doc.get("similarity", 0) * 100)
                tags = doc.get("tags", [])
                subj = [t["name"] for t in tags if t["tag_type"] == "subject"]
                skls = [t["name"] for t in tags if t["tag_type"] == "skill"]
                diff_en = doc.get("difficulty", "")
                diff_display = translate_difficulty(diff_en)
                dcls = f"tag-difficulty-{diff_en}"
                st.markdown(f"""
                <div class='vault-card'>
                  <div style='display:flex;justify-content:space-between;align-items:flex-start;gap:1rem'>
                    <div style='flex:1'>
                      <div class='card-title'>{doc['filename']}</div>
                      <div class='card-desc'>{doc.get('description','')}</div>
                    </div>
                    <span class='difficulty-badge {dcls}'>{diff_display}</span>
                  </div>
                  <div style='margin-top:1rem'>
                    {"".join(f"<span class='tag-subject'>{translate_tag(s)}</span>" for s in subj)}
                    {"".join(f"<span class='tag-skill'>{translate_tag(s)}</span>" for s in skls[:6])}
                  </div>
                  <div style='margin-top:1rem'>
                    <div style='color:#6d28d9;font-size:0.7rem;letter-spacing:0.1em;font-weight:600'>{T('relevance')} &nbsp; {sim}%</div>
                    <div class='bar-bg'><div class='bar-fill' style='width:{sim}%'></div></div>
                  </div>
                </div>
                """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# LIBRARY
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Library":
    page_title("library_title")
    from db.supabase_client import get_all_documents, delete_document
    try:
        docs = get_all_documents()
    except Exception as e:
        st.error(f"{T('lib_load_fail')} {e}")
        docs = []

    if not docs:
        empty_lines = T("lib_empty").replace("\n", "<br>")
        st.markdown(f"<div class='empty-state'>{empty_lines}</div>", unsafe_allow_html=True)
    else:
        count = len(docs)
        count_label = T("doc_singular") if count == 1 else T("docs_in_vault")
        st.markdown(f"<div class='section-label'>{count} {count_label}</div>", unsafe_allow_html=True)

        for doc in docs:
            tags = doc.get("tags", [])
            subj = [t["name"] for t in tags if t["tag_type"] == "subject"]
            skls = [t["name"] for t in tags if t["tag_type"] == "skill"]
            diff_en = doc.get("difficulty", "")
            diff_display = translate_difficulty(diff_en)
            dcls = f"tag-difficulty-{diff_en}"
            with st.expander(f"  {doc['filename']}", expanded=False):
                c1, c2 = st.columns([3, 1])
                with c1:
                    st.markdown(f"<div class='card-desc' style='margin-bottom:1.2rem'>{doc.get('description', T('no_desc'))}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='section-label'>{T('subjects_label')}</div>" + " ".join(f"<span class='tag-subject'>{translate_tag(s)}</span>" for s in subj), unsafe_allow_html=True)
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.markdown(f"<div class='section-label'>{T('skills_label')}</div>" + " ".join(f"<span class='tag-skill'>{translate_tag(s)}</span>" for s in skls), unsafe_allow_html=True)
                with c2:
                    st.markdown(f"<span class='difficulty-badge {dcls}'>{diff_display}</span>", unsafe_allow_html=True)
                    st.markdown("")
                    if st.button(T("delete_btn"), key=f"del_{doc['id']}"):
                        try:
                            delete_document(doc["id"])
                            st.success(T("deleted_ok"))
                            st.rerun()
                        except Exception as e:
                            st.error(f"{T('delete_fail')} {e}")

# ══════════════════════════════════════════════════════════════════════════════
# BROWSE BY TAG
# ══════════════════════════════════════════════════════════════════════════════
elif page == "Browse by Tag":
    page_title("browse_title")
    from db.supabase_client import get_all_tags, get_documents_by_tag
    try:
        all_tags = get_all_tags()
    except Exception as e:
        st.error(f"{T('tags_load_fail')} {e}")
        all_tags = {"subject": [], "skill": []}

    cl, cr = st.columns([1, 2])
    all_opt = T("all_option")

    with cl:
        st.markdown(f"<div class='section-label'>{T('by_subject')}</div>", unsafe_allow_html=True)
        subj_display = [all_opt] + [translate_tag(s) for s in all_tags["subject"]]
        subj_raw     = [None]    + all_tags["subject"]
        sel_sub_disp = st.radio("Subject", subj_display, label_visibility="collapsed")
        sel_sub = subj_raw[subj_display.index(sel_sub_disp)]

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"<div class='section-label'>{T('by_skill')}</div>", unsafe_allow_html=True)
        skl_display = [all_opt] + [translate_tag(s) for s in all_tags["skill"]]
        skl_raw     = [None]    + all_tags["skill"]
        sel_skl_disp = st.radio("Skill", skl_display, label_visibility="collapsed")
        sel_skl = skl_raw[skl_display.index(sel_skl_disp)]

    with cr:
        active = None
        if sel_sub is not None:
            active = ("subject", sel_sub)
        elif sel_skl is not None:
            active = ("skill", sel_skl)

        if active:
            try:
                docs = get_documents_by_tag(*active)
            except Exception as e:
                st.error(f"{T('filter_fail')} {e}")
                docs = []
            _, tag_name = active
            st.markdown(f"<div class='section-label'>{T('tagged_label')} {translate_tag(tag_name)}</div>", unsafe_allow_html=True)
            if not docs:
                st.markdown(f"<div class='empty-state'>{T('no_tag_docs')}</div>", unsafe_allow_html=True)
            else:
                for doc in docs:
                    tags = doc.get("tags", [])
                    subj = [t["name"] for t in tags if t["tag_type"] == "subject"]
                    skls = [t["name"] for t in tags if t["tag_type"] == "skill"]
                    diff_en = doc.get("difficulty", "")
                    diff_display = translate_difficulty(diff_en)
                    dcls = f"tag-difficulty-{diff_en}"
                    st.markdown(f"""
                    <div class='vault-card'>
                      <div style='display:flex;justify-content:space-between;gap:1rem'>
                        <div class='card-title'>{doc['filename']}</div>
                        <span class='difficulty-badge {dcls}'>{diff_display}</span>
                      </div>
                      <div class='card-desc'>{doc.get('description','')}</div>
                      <div style='margin-top:0.9rem'>
                        {"".join(f"<span class='tag-subject'>{translate_tag(s)}</span>" for s in subj)}
                        {"".join(f"<span class='tag-skill'>{translate_tag(s)}</span>" for s in skls)}
                      </div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='empty-state'>{T('pick_tag')}</div>", unsafe_allow_html=True)
