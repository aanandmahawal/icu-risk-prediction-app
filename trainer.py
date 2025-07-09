import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from tabpfn import TabPFNClassifier

def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    st.write(f"**Train Samples**: {X_train.shape[0]} | **Test Samples**: {X_test.shape[0]}")

    clf = TabPFNClassifier(device='cpu')
    clf.fit(X_train.to_numpy(), y_train)

    y_pred = clf.predict(X_test.to_numpy())

    acc = accuracy_score(y_test, y_pred)
    st.metric(label="✅ Accuracy", value=f"{acc*100:.2f}%")

    st.subheader("📋 Classification Report")
    report = classification_report(y_test, y_pred, output_dict=True)
    st.dataframe(report)

    # ✅ Inline Confusion Matrix display
    show_accuracy_matrix(y_test, y_pred)

    return clf, y_test, y_pred


# ✅ Confusion matrix function now lives here
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

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
