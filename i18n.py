"""
i18n.py — UI string translations for Knowledge Vault
Supports: English (en), Telugu (te), Hindi (hi)

Usage:
    from i18n import T
    T("search_title")          # uses current language from session state
    T("search_title", "te")    # force Telugu
"""

import streamlit as st

STRINGS = {

    # ── Sidebar ──────────────────────────────────────────────────────────────
    "nav_label":        {"en": "Navigate",          "te": "నావిగేట్",        "hi": "नेविगेट"},
    "nav_home":         {"en": "🏠  Home",           "te": "🏠  హోమ్",        "hi": "🏠  होम"},
    "nav_search":       {"en": "🔍  Search",         "te": "🔍  వెతకండి",     "hi": "🔍  खोजें"},
    "nav_library":      {"en": "📚  Library",        "te": "📚  లైబ్రరీ",     "hi": "📚  पुस्तकालय"},
    "nav_browse":       {"en": "🏷️  Browse by Tag",  "te": "🏷️  ట్యాగ్ చూడండి", "hi": "🏷️  टैग से खोजें"},
    "nav_upload":       {"en": "📤  Upload",         "te": "📤  అప్లోడ్",     "hi": "📤  अपलोड"},
    "lang_label":       {"en": "Language",           "te": "భాష",             "hi": "भाषा"},
    "ai_provider":      {"en": "AI Provider",        "te": "AI ప్రొవైడర్",    "hi": "AI प्रदाता"},
    "key_set":          {"en": "✓ Key set",          "te": "✓ కీ సెట్ అయింది","hi": "✓ की सेट है"},
    "no_key":           {"en": "⚠ No key — add one above or set GROQ_API_KEY in .env",
                         "te": "⚠ కీ లేదు — పైన జోడించండి లేదా .env లో GROQ_API_KEY సెట్ చేయండి",
                         "hi": "⚠ की नहीं — ऊपर जोड़ें या .env में GROQ_API_KEY सेट करें"},
    "ollama_hint":      {"en": "Make sure Ollama is running locally and the model is pulled.",
                         "te": "Ollama స్థానికంగా నడుస్తుందని మరియు మోడల్ పుల్ చేయబడిందని నిర్ధారించుకోండి.",
                         "hi": "सुनिश्चित करें कि Ollama स्थानीय रूप से चल रहा है और मॉडल pull किया गया है।"},
    "tagline":          {"en": "Upload once.\nFind anything.\nAI does the rest.",
                         "te": "ఒకసారి అప్లోడ్ చేయండి.\nఏదైనా కనుగొనండి.\nAI మిగతాది చేస్తుంది.",
                         "hi": "एक बार अपलोड करें.\nकुछ भी खोजें.\nबाकी AI करेगा।"},

    # ── Home page ─────────────────────────────────────────────────────────────
    "hero_eyebrow":     {"en": "✦  AI-Powered Document Library  ✦",
                         "te": "✦  AI-ఆధారిత డాక్యుమెంట్ లైబ్రరీ  ✦",
                         "hi": "✦  AI-संचालित दस्तावेज़ पुस्तकालय  ✦"},
    "hero_title":       {"en": "Knowledge Vault",
                         "te": "నాలెడ్జ్ వాల్ట్",
                         "hi": "नॉलेज वॉल्ट"},
    "hero_sub":         {"en": "Your documents, intelligently organised.",
                         "te": "మీ పత్రాలు, తెలివిగా వ్యవస్థీకరించబడ్డాయి.",
                         "hi": "आपके दस्तावेज़, बुद्धिमानी से व्यवस्थित।"},
    "get_started":      {"en": "Get started",        "te": "ప్రారంభించండి",   "hi": "शुरू करें"},
    "upload_btn":       {"en": "✦  Upload a Document","te": "✦  డాక్యుమెంట్ అప్లోడ్ చేయండి", "hi": "✦  दस्तावेज़ अपलोड करें"},
    "how_it_works":     {"en": "How it works",       "te": "ఇది ఎలా పని చేస్తుంది", "hi": "यह कैसे काम करता है"},
    "intro_text":       {
        "en": "Stop drowning in unsorted PDFs, lecture notes, and articles. Knowledge Vault reads every document you upload and automatically assigns <strong style='color:#e9d5ff'>subject tags</strong>, <strong style='color:#e9d5ff'>skill tags</strong>, and a <strong style='color:#e9d5ff'>difficulty level</strong> — no manual effort needed. When you want to learn something new, just search and the vault surfaces exactly which documents to read, ranked by relevance.",
        "te": "క్రమం లేని PDFలు, లెక్చర్ నోట్స్ మరియు వ్యాసాలలో మునిగిపోవడం మానేయండి. Knowledge Vault మీరు అప్లోడ్ చేసే ప్రతి పత్రాన్ని చదివి, స్వయంచాలకంగా <strong style='color:#e9d5ff'>సబ్జెక్ట్ ట్యాగ్‌లు</strong>, <strong style='color:#e9d5ff'>స్కిల్ ట్యాగ్‌లు</strong> మరియు <strong style='color:#e9d5ff'>కష్టత స్థాయి</strong> కేటాయిస్తుంది. మీరు కొత్తది నేర్చుకోవాలనుకున్నప్పుడు, వెతకండి — వాల్ట్ సంబంధిత పత్రాలను ర్యాంక్ చేసి చూపుతుంది.",
        "hi": "अनसॉर्टेड PDFs, लेक्चर नोट्स और लेखों में खोने से बचें। Knowledge Vault आपके हर अपलोड किए गए दस्तावेज़ को पढ़कर स्वचालित रूप से <strong style='color:#e9d5ff'>विषय टैग</strong>, <strong style='color:#e9d5ff'>कौशल टैग</strong> और एक <strong style='color:#e9d5ff'>कठिनाई स्तर</strong> देता है — कोई मैन्युअल काम नहीं। जब आप कुछ नया सीखना चाहें, बस खोजें और vault सही दस्तावेज़ दिखाएगा।"
    },
    "step_upload":      {"en": "Upload",             "te": "అప్లోడ్",          "hi": "अपलोड"},
    "step_upload_desc": {"en": "PDF, DOCX, or TXT",  "te": "PDF, DOCX లేదా TXT","hi": "PDF, DOCX या TXT"},
    "step_ai":          {"en": "AI analyses",        "te": "AI విశ్లేషిస్తుంది","hi": "AI विश्लेषण"},
    "step_ai_desc":     {"en": "Tags subjects, skills & level",
                         "te": "సబ్జెక్టులు, స్కిల్స్ & స్థాయి ట్యాగ్ చేస్తుంది",
                         "hi": "विषय, कौशल और स्तर टैग करता है"},
    "step_search":      {"en": "Search",             "te": "వెతకండి",          "hi": "खोजें"},
    "step_search_desc": {"en": "Find by concept, not keyword",
                         "te": "కీవర్డ్ కాదు, భావన ద్వారా కనుగొనండి",
                         "hi": "कीवर्ड नहीं, अवधारणा से खोजें"},
    "step_discover":    {"en": "Discover",           "te": "కనుగొనండి",        "hi": "खोजें"},
    "step_discover_desc":{"en": "Know exactly what to read",
                          "te": "ఏమి చదవాలో సరిగ్గా తెలుసుకోండి",
                          "hi": "जानें कि क्या पढ़ना है"},

    # ── Upload page ───────────────────────────────────────────────────────────
    "upload_title":     {"en": "Upload a document",  "te": "డాక్యుమెంట్ అప్లోడ్ చేయండి", "hi": "दस्तावेज़ अपलोड करें"},
    "upload_hint":      {"en": "Drop in a PDF, DOCX, or TXT — the AI will read it and automatically assign subjects, skills, and difficulty. No manual tagging needed.",
                         "te": "PDF, DOCX లేదా TXT వేయండి — AI దాన్ని చదివి సబ్జెక్టులు, స్కిల్స్ మరియు కష్టత స్వయంచాలకంగా కేటాయిస్తుంది. మాన్యువల్ ట్యాగింగ్ అవసరం లేదు.",
                         "hi": "PDF, DOCX या TXT डालें — AI इसे पढ़कर विषय, कौशल और कठिनाई स्वचालित रूप से देगा। मैन्युअल टैगिंग की जरूरत नहीं।"},
    "analyse_btn":      {"en": "✦  Analyse & Add to Vault",
                         "te": "✦  విశ్లేషించండి & వాల్ట్‌కు జోడించండి",
                         "hi": "✦  विश्लेषण करें और Vault में जोड़ें"},
    "analysing":        {"en": "Reading and analysing",  "te": "చదువుతోంది మరియు విశ్లేషిస్తోంది", "hi": "पढ़ रहा है और विश्लेषण कर रहा है"},
    "added_ok":         {"en": "✓ Added to vault",   "te": "✓ వాల్ట్‌కు జోడించబడింది", "hi": "✓ Vault में जोड़ा गया"},
    "what_covers":      {"en": "What this document covers",
                         "te": "ఈ పత్రం ఏమి కవర్ చేస్తుంది",
                         "hi": "यह दस्तावेज़ क्या कवर करता है"},
    "level_label":      {"en": "Level",              "te": "స్థాయి",           "hi": "स्तर"},
    "subjects_label":   {"en": "Subjects",           "te": "సబ్జెక్టులు",      "hi": "विषय"},
    "skills_label":     {"en": "Skills detected",    "te": "స్కిల్స్ కనుగొనబడ్డాయి", "hi": "कौशल पाए गए"},
    "coverage_label":   {"en": "coverage",           "te": "కవరేజ్",           "hi": "कवरेज"},
    "err_process":      {"en": "Could not process file:",  "te": "ఫైల్ ప్రాసెస్ చేయలేకపోయాం:", "hi": "फ़ाइल प्रोसेस नहीं हो सकी:"},
    "err_generic":      {"en": "Something went wrong:", "te": "ఏదో తప్పు జరిగింది:", "hi": "कुछ गलत हो गया:"},

    # ── Search page ───────────────────────────────────────────────────────────
    "search_title":     {"en": "Search your vault",  "te": "మీ వాల్ట్ వెతకండి", "hi": "अपना Vault खोजें"},
    "search_hint":      {"en": "Describe what you want to learn. The AI finds relevant documents even without exact keyword matches.",
                         "te": "మీరు ఏమి నేర్చుకోవాలనుకుంటున్నారో వివరించండి. సరైన కీవర్డ్‌లు లేకుండా కూడా AI సంబంధిత పత్రాలను కనుగొంటుంది.",
                         "hi": "बताएं कि आप क्या सीखना चाहते हैं। बिना सटीक कीवर्ड के भी AI प्रासंगिक दस्तावेज़ खोज लेगा।"},
    "search_placeholder":{"en": "e.g.  gradient descent  ·  sorting algorithms  ·  probability distributions",
                          "te": "ఉదా.  గ్రేడియంట్ డిసెంట్  ·  సార్టింగ్ అల్గారిథమ్స్  ·  సంభావ్యత పంపిణీ",
                          "hi": "जैसे  gradient descent  ·  sorting algorithms  ·  probability"},
    "searching":        {"en": "Searching your vault…", "te": "మీ వాల్ట్ వెతుకుతోంది…", "hi": "आपका Vault खोज रहा है…"},
    "search_fail":      {"en": "Search failed:",     "te": "శోధన విఫలమైంది:",   "hi": "खोज विफल रही:"},
    "no_results":       {"en": "Nothing found — try uploading some documents first.",
                         "te": "ఏమీ కనుగొనలేదు — ముందు కొన్ని పత్రాలు అప్లోడ్ చేయండి.",
                         "hi": "कुछ नहीं मिला — पहले कुछ दस्तावेज़ अपलोड करें।"},
    "results_for":      {"en": "results for",        "te": "ఫలితాలు",           "hi": "परिणाम"},
    "result_singular":  {"en": "result for",         "te": "ఫలితం",             "hi": "परिणाम"},
    "relevance":        {"en": "RELEVANCE",          "te": "సంబంధం",            "hi": "प्रासंगिकता"},

    # ── Library page ──────────────────────────────────────────────────────────
    "library_title":    {"en": "Your library",       "te": "మీ లైబ్రరీ",       "hi": "आपकी लाइब्रेरी"},
    "lib_load_fail":    {"en": "Could not load library:", "te": "లైబ్రరీ లోడ్ కాలేదు:", "hi": "लाइब्रेरी लोड नहीं हो सकी:"},
    "lib_empty":        {"en": "Your vault is empty.\nHead to Upload to add your first document.",
                         "te": "మీ వాల్ట్ ఖాళీగా ఉంది.\nమీ మొదటి పత్రాన్ని జోడించడానికి అప్లోడ్‌కు వెళ్ళండి.",
                         "hi": "आपका Vault खाली है।\nपहला दस्तावेज़ जोड़ने के लिए Upload पर जाएं।"},
    "docs_in_vault":    {"en": "documents in your vault", "te": "పత్రాలు మీ వాల్ట్‌లో ఉన్నాయి", "hi": "दस्तावेज़ आपके Vault में"},
    "doc_singular":     {"en": "document in your vault",  "te": "పత్రం మీ వాల్ట్‌లో ఉంది",  "hi": "दस्तावेज़ आपके Vault में"},
    "no_desc":          {"en": "No description.",    "te": "వివరణ లేదు.",       "hi": "कोई विवरण नहीं।"},
    "delete_btn":       {"en": "Delete",             "te": "తొలగించు",          "hi": "हटाएं"},
    "deleted_ok":       {"en": "Deleted.",           "te": "తొలగించబడింది.",    "hi": "हटा दिया गया।"},
    "delete_fail":      {"en": "Delete failed:",     "te": "తొలగింపు విఫలమైంది:", "hi": "हटाना विफल रहा:"},

    # ── Browse by Tag page ────────────────────────────────────────────────────
    "browse_title":     {"en": "Browse by tag",      "te": "ట్యాగ్ ద్వారా చూడండి", "hi": "टैग से ब्राउज़ करें"},
    "tags_load_fail":   {"en": "Could not load tags:", "te": "ట్యాగ్‌లు లోడ్ కాలేదు:", "hi": "टैग लोड नहीं हो सके:"},
    "by_subject":       {"en": "By subject",         "te": "సబ్జెక్ట్ ద్వారా",  "hi": "विषय से"},
    "by_skill":         {"en": "By skill",           "te": "స్కిల్ ద్వారా",     "hi": "कौशल से"},
    "all_option":       {"en": "(all)",              "te": "(అన్నీ)",            "hi": "(सभी)"},
    "tagged_label":     {"en": "Tagged —",           "te": "ట్యాగ్ చేయబడింది —", "hi": "टैग किया —"},
    "no_tag_docs":      {"en": "No documents with this tag yet.",
                         "te": "ఈ ట్యాగ్‌తో ఇంకా పత్రాలు లేవు.",
                         "hi": "इस टैग के साथ अभी कोई दस्तावेज़ नहीं।"},
    "pick_tag":         {"en": "Select a subject or skill on the left to filter your vault.",
                         "te": "మీ వాల్ట్‌ను ఫిల్టర్ చేయడానికి ఎడమ వైపు ఒక సబ్జెక్ట్ లేదా స్కిల్ ఎంచుకోండి.",
                         "hi": "अपना Vault फ़िल्टर करने के लिए बाईं ओर एक विषय या कौशल चुनें।"},
    "filter_fail":      {"en": "Filter failed:",     "te": "ఫిల్టర్ విఫలమైంది:", "hi": "फ़िल्टर विफल रहा:"},

    # ── Difficulty labels (displayed on-screen only) ───────────────────────────
    "Beginner":         {"en": "Beginner",           "te": "ప్రారంభకుడు",      "hi": "शुरुआती"},
    "Intermediate":     {"en": "Intermediate",       "te": "మధ్యస్థం",         "hi": "मध्यम"},
    "Advanced":         {"en": "Advanced",           "te": "అధునాతన",           "hi": "उन्नत"},
}

# Common tag translations — shown on-screen only, never stored in DB
TAG_TRANSLATIONS = {
    # Subjects
    "Mathematics":          {"te": "గణితం",              "hi": "गणित"},
    "Machine Learning":     {"te": "మెషీన్ లెర్నింగ్",   "hi": "मशीन लर्निंग"},
    "Programming":          {"te": "ప్రోగ్రామింగ్",      "hi": "प्रोग्रामिंग"},
    "Physics":              {"te": "భౌతిక శాస్త్రం",    "hi": "भौतिकी"},
    "Statistics":           {"te": "గణాంకాలు",           "hi": "सांख्यिकी"},
    "Data Science":         {"te": "డేటా సైన్స్",        "hi": "डेटा विज्ञान"},
    "Computer Science":     {"te": "కంప్యూటర్ సైన్స్",   "hi": "कंप्यूटर विज्ञान"},
    "Linear Algebra":       {"te": "లీనియర్ ఆల్జీబ్రా",  "hi": "रैखिक बीजगणित"},
    "Calculus":             {"te": "కాలిక్యులస్",        "hi": "कलन"},
    "Signal Processing":    {"te": "సిగ్నల్ ప్రాసెసింగ్","hi": "संकेत प्रसंस्करण"},
    "Deep Learning":        {"te": "డీప్ లెర్నింగ్",     "hi": "गहरी शिक्षा"},
    "Networking":           {"te": "నెట్‌వర్కింగ్",      "hi": "नेटवर्किंग"},
    "Algorithms":           {"te": "అల్గారిథమ్స్",       "hi": "एल्गोरिदम"},
    # Skills
    "Gradient descent":     {"te": "గ్రేడియంట్ డిసెంట్", "hi": "ग्रेडिएंट डिसेंट"},
    "Backpropagation":      {"te": "బ్యాక్‌ప్రొపగేషన్",  "hi": "बैकप्रोपेगेशन"},
    "Matrix operations":    {"te": "మాత్రిక్స్ ఆపరేషన్స్","hi": "मैट्रिक्स संक्रियाएं"},
    "Eigenvalues":          {"te": "ఐగన్‌వాల్యూలు",      "hi": "eigenvalues"},
    "NumPy":                {"te": "న్యూమ్‌పై",           "hi": "NumPy"},
    "Data cleaning":        {"te": "డేటా క్లీనింగ్",     "hi": "डेटा सफाई"},
    "Fourier Transform":    {"te": "ఫోరియర్ ట్రాన్స్ఫార్మ్","hi": "फ़ूरियर ट्रांसफ़ॉर्म"},
    "Sampling":             {"te": "శాంప్లింగ్",          "hi": "सैंपलिंग"},
    "Convolution":          {"te": "కన్వల్యూషన్",        "hi": "कनवल्यूशन"},
    "Neural networks":      {"te": "న్యూరల్ నెట్‌వర్క్స్","hi": "तंत्रिका जाल"},
    "Probability":          {"te": "సంభావ్యత",            "hi": "प्रायिकता"},
    "Recursion":            {"te": "రికర్షన్",            "hi": "पुनरावृत्ति"},
    "Sorting":              {"te": "సార్టింగ్",           "hi": "क्रमबद्धता"},
}


def T(key: str, lang: str = None) -> str:
    """
    Return the UI string for key in the current (or given) language.
    Falls back to English if key or language is missing.
    """
    if lang is None:
        lang = st.session_state.get("lang", "en")
    entry = STRINGS.get(key, {})
    return entry.get(lang) or entry.get("en") or key


def translate_tag(tag: str, lang: str = None) -> str:
    """
    Return the translated version of a tag name for display only.
    Falls back to the original English tag if no translation exists.
    """
    if lang is None:
        lang = st.session_state.get("lang", "en")
    if lang == "en":
        return tag
    return TAG_TRANSLATIONS.get(tag, {}).get(lang, tag)


def translate_difficulty(diff: str, lang: str = None) -> str:
    """Translate difficulty label (Beginner/Intermediate/Advanced)."""
    if lang is None:
        lang = st.session_state.get("lang", "en")
    return T(diff, lang) if diff else diff
