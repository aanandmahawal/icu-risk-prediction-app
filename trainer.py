import streamlit as st
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

def show_accuracy_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    acc = accuracy_score(y_true, y_pred)

    fig, ax = plt.subplots(figsize=(4, 3))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No ICU", "ICU"])
    disp.plot(ax=ax, cmap='Greens', colorbar=False)
    ax.set_title(f"Confusion Matrix\nAccuracy: {acc*100:.2f}%")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    plt.tight_layout()

    st.subheader("📉 Model Evaluation: Confusion Matrix")
    st.pyplot(fig)
    st.metric(label="✅ Accuracy", value=f"{acc*100:.2f}%")
