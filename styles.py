def load_css():

    return """
    <style>

    /* Hide Streamlit Branding */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* Main App */

    .main {
        background: linear-gradient(
            135deg,
            #f4f7fa,
            #eef7ff
        );
    }

    /* Title */

    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: #0f172a;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 18px;
        margin-bottom: 25px;
    }

    /* Cards */

    .health-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(
            0,
            0,
            0,
            0.08
        );
        margin-bottom: 15px;
    }

    /* Prediction Result */

    .risk-high {
        background: #fee2e2;
        color: #b91c1c;
        padding: 18px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
    }

    .risk-medium {
        background: #fef3c7;
        color: #b45309;
        padding: 18px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
    }

    .risk-low {
        background: #dcfce7;
        color: #15803d;
        padding: 18px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 600;
        text-align: center;
    }

    /* Sidebar */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #0f172a,
            #1e293b
        );
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Chat */

    .chat-header {
        font-size: 30px;
        font-weight: 700;
        color: #0f172a;
        text-align: center;
        margin-bottom: 15px;
    }

    .medical-warning {
        background: #fff7ed;
        border-left: 5px solid #ea580c;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
    }

    /* Metric Cards */

    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(
            0,
            0,
            0,
            0.05
        );
    }

    /* Buttons */

    .stButton button {
        width: 100%;
        border-radius: 12px;
        font-weight: 600;
        padding: 10px;
    }

    /* Chat Input */

    .stChatInputContainer {
        border-radius: 15px;
    }

    </style>
    """