import streamlit as st
from data_generator import generate_synthetic_data
from trainer import train_and_evaluate, show_accuracy_matrix  # ✅ Updated import
from predictor import streamlit_predict_custom_input

# 🔧 CSS: Remove top padding for cleaner title layout
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🩺 ICU Risk Prediction App")

# Tabs: [Data & Training], [Model Evaluation], [Custom Prediction]
tabs = st.tabs(["📁 Data & Training", "📊 Model Evaluation", "🔮 Custom Prediction"])

# -------------------------------
#  Tab 1: Data & Training
# -------------------------------
with tabs[0]:
    st.subheader("📁 Generate Data and Train the Model")

    if st.button("Generate Synthetic Data"):
        st.session_state.X, st.session_state.y = generate_synthetic_data()
        st.success("✅ Synthetic data generated!")

    if "X" in st.session_state and "y" in st.session_state:
        if st.button("Train Model"):
            clf, y_test, y_pred = train_and_evaluate(st.session_state.X, st.session_state.y)
            st.session_state.clf = clf
            st.session_state.y_test = y_test
            st.session_state.y_pred = y_pred
            st.success("✅ Model trained and evaluation complete!")

# -------------------------------
#  Tab 2: Model Evaluation
# -------------------------------
with tabs[1]:
    st.subheader("📊 Model Performance Metrics")
    if "y_test" in st.session_state and "y_pred" in st.session_state:
        show_accuracy_matrix(st.session_state.y_test, st.session_state.y_pred)
    else:
        st.warning("⚠️ Please train the model first.")

# -------------------------------
#  Tab 3: ICU Prediction
# -------------------------------
with tabs[2]:
    st.subheader(" Predict ICU Risk from Custom Input")
    if "clf" in st.session_state:
        streamlit_predict_custom_input(st.session_state.clf)
    else:
        st.info("ℹ️ Train the model to enable ICU prediction.")
