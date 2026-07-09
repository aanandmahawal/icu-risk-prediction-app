def load_css():

    return """
    <style>

    /* ---------------------------
       Streamlit Cleanup
    --------------------------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* IMPORTANT:
       Do NOT hide header.
       Streamlit uses it for sidebar toggle.
    */

    header[data-testid="stHeader"] {
        background: rgba(255,255,255,0);
    }

    /* ---------------------------
       Main Background
    --------------------------- */

    .stApp {
        background: linear-gradient(
            135deg,
            #f8fbff,
            #eef6ff
        );
    }

    /* ---------------------------
       Title
    --------------------------- */

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #475569;
        font-size: 18px;
        margin-bottom: 20px;
    }

    /* ---------------------------
       Cards
    --------------------------- */

    .health-card {
        background: white;
        padding: 20px;
        border-radius: 18px;
        border: 1px solid #dbeafe;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }

    /* ---------------------------
       Sidebar
    --------------------------- */

    section[data-testid="stSidebar"] {
        background: #f8fafc !important;
        border-right: 1px solid #dbeafe;
    }

    section[data-testid="stSidebar"] * {
        color: #0f172a !important;
    }

    /* ---------------------------
       Sidebar Buttons
    --------------------------- */

    section[data-testid="stSidebar"] .stButton button {

        background: white !important;
        color: #0f172a !important;

        border: 1px solid #cbd5e1 !important;

        border-radius: 10px;

        font-weight: 600;
    }

    section[data-testid="stSidebar"] .stButton button:hover {

        border: 1px solid #2563eb !important;

        color: #2563eb !important;
    }

    /* ---------------------------
       Global Buttons
    --------------------------- */

    .stButton button {

        border-radius: 12px;

        font-weight: 600;

        padding: 0.6rem;
    }

    /* ---------------------------
       Chat
    --------------------------- */

    .chat-header {

        text-align: center;

        font-size: 32px;

        font-weight: 700;

        color: #0f172a;

        margin-bottom: 10px;
    }

    .medical-warning {

        background: #fff7ed;

        border-left: 5px solid #ea580c;

        padding: 15px;

        border-radius: 10px;

        margin-bottom: 20px;
    }

    /* ---------------------------
       Navigation Bar
    --------------------------- */

    div[role="radiogroup"] {

        padding: 10px;

        border-radius: 15px;

        background: white;

        border: 1px solid #dbeafe;

        margin-bottom: 15px;
    }

    /* ---------------------------
       Metrics
    --------------------------- */

    [data-testid="stMetric"] {

        background: white;

        border-radius: 15px;

        padding: 10px;

        border: 1px solid #dbeafe;
    }

    </style>
    """
