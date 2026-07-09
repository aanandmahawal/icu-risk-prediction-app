import streamlit as st
import os
import joblib

from predictor import streamlit_predict_custom_input
from chatbot import get_medical_response
from styles import load_css

MODEL_PATH = "xgb_icu_model.pkl.gz"

# ===================================================
# PAGE CONFIG
# ===================================================

st.set_page_config(
    page_title="AI Healthcare Assistant",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================================================
# CSS
# ===================================================

st.markdown(load_css(), unsafe_allow_html=True)

# ===================================================
# SESSION STATE
# ===================================================

if "page" not in st.session_state:
    st.session_state.page = "ICU Risk Predictor"

if "messages" not in st.session_state:
    st.session_state.messages = []

# ===================================================
# LOAD MODEL
# ===================================================

if "clf" not in st.session_state:
    if os.path.exists(MODEL_PATH):
        st.session_state.clf = joblib.load(MODEL_PATH)
    else:
        st.error("Model file not found.")

# ===================================================
# SIDEBAR
# ===================================================

with st.sidebar:

    st.markdown("## 🏥 Healthcare AI")

    if st.button("📈 ICU Predictor", use_container_width=True):
        st.session_state.page = "ICU Risk Predictor"

    if st.button("🤖 Medical Chatbot", use_container_width=True):
        st.session_state.page = "Medical AI Chatbot"

    if st.button("📖 About", use_container_width=True):
        st.session_state.page = "About"

    st.markdown("---")

    if st.button("🗑 Clear Chat History", use_container_width=True):

        st.session_state.messages = []

        if st.session_state.page == "Medical AI Chatbot":
            st.rerun()

    st.markdown("---")

    st.info(
        """
        AI-powered healthcare assistant

        ✔ ICU Risk Prediction
        ✔ Medical AI Chatbot
        ✔ Health Education
        """
    )

# ===================================================
# HEADER
# ===================================================

st.markdown(
    """
    <div class="main-title">
        🏥 AI Healthcare Assistant
    </div>

    <div class="subtitle">
        ICU Risk Prediction + Medical AI Chatbot
    </div>
    """,
    unsafe_allow_html=True
)

# ===================================================
# ALWAYS VISIBLE NAVIGATION
# ===================================================

nav1, nav2, nav3 = st.columns(3)

with nav1:
    if st.button("📈 Predictor", use_container_width=True):
        st.session_state.page = "ICU Risk Predictor"

with nav2:
    if st.button("🤖 Chatbot", use_container_width=True):
        st.session_state.page = "Medical AI Chatbot"

with nav3:
    if st.button("📖 About", use_container_width=True):
        st.session_state.page = "About"

st.markdown("---")

page = st.session_state.page

# ===================================================
# PAGE 1
# ===================================================

if page == "ICU Risk Predictor":

    st.markdown(
        """
        <div class="health-card">
            <h3>📈 ICU Risk Prediction</h3>
            Enter patient vitals and clinical information
            to estimate ICU admission risk.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model", "XGBoost")

    with col2:
        st.metric("Use Case", "ICU Triage")

    with col3:
        st.metric("Prediction", "Real-Time")

    st.markdown("---")

    if "clf" in st.session_state:
        streamlit_predict_custom_input(
            st.session_state.clf
        )
    else:
        st.warning("Model not loaded.")

# ===================================================
# PAGE 2
# ===================================================

elif page == "Medical AI Chatbot":

    title_col1, title_col2 = st.columns([5, 1])

    with title_col1:

        st.markdown(
            """
            <div class="chat-header">
                🤖 Medical AI Assistant
            </div>
            """,
            unsafe_allow_html=True
        )

    with title_col2:

        if st.button(
            "🗑 New Chat",
            use_container_width=True
        ):
            st.session_state.messages = []
            st.rerun()

    st.markdown(
        """
        <div class="medical-warning">
        ⚠️ This AI provides educational information only.
        It does NOT replace professional medical advice.
        For emergencies, contact a healthcare professional immediately.
        </div>
        """,
        unsafe_allow_html=True
    )

    if len(st.session_state.messages) == 0:

        st.info(
            """
            Try asking:

            • What are symptoms of diabetes?
            • Explain high blood pressure.
            • What causes fever and headache?
            • How can I improve heart health?
            """
        )

    # CHAT HISTORY

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input(
        "Ask a medical question..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("🩺 Analyzing..."):

                response = get_medical_response(
                    prompt
                )

                st.markdown(response)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

# ===================================================
# PAGE 3
# ===================================================

elif page == "About":

    st.markdown(
        """
        <div class="health-card">
            <h2>📖 About the Project</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
### 🔬 ICU Risk Prediction

Predicts ICU admission risk using an XGBoost model trained on patient vital signs.

#### Inputs
- Heart Rate
- Blood Pressure
- Temperature
- Respiratory Rate
- Comorbidity Index

---

### 🤖 Medical AI Chatbot

Powered by:
- Groq API
- Llama 3.1
- Streamlit

Capabilities:
- Symptom explanations
- Disease information
- Medical education
- Health guidance

---

### ⚠ Disclaimer

This application is intended for educational and demonstration purposes only.

It does not diagnose, prescribe, or replace professional medical consultation.

---

### 🛠 Tech Stack

- Python
- Streamlit
- XGBoost
- Groq API
- Llama 3.1
- Joblib
""")

    st.success(
        "Built with Machine Learning + Generative AI"
    )
