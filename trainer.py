# trainer.py

import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from xgboost import XGBClassifier
import joblib
import gzip
import os

MODEL_PATH = "xgb_icu_model.pkl.gz"

def train_and_evaluate(X, y):
    """
    Train XGBoost model and save as compressed .pkl.gz (<5MB).
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    st.write(f"Train Samples: {X_train.shape[0]} | Test Samples: {X_test.shape[0]}")

    # XGBoost model
    clf = XGBClassifier(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1,
        use_label_encoder=False,
        eval_metric='logloss'
    )
    clf.fit(X_train, y_train)

    # Save compressed model
    os.makedirs("model", exist_ok=True)
    with gzip.open(MODEL_PATH, "wb", compresslevel=9) as f:
        joblib.dump(clf, f)
    st.success(f"✅ Compressed model saved to `{MODEL_PATH}`")

    # Evaluate
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    st.metric(label="Accuracy", value=f"{acc*100:.2f}%")

    st.subheader("Classification Report")
    report = classification_report(y_test, y_pred, output_dict=True)
    st.dataframe(report)

    show_accuracy_matrix(y_test, y_pred)
    return clf, y_test, y_pred


def show_accuracy_matrix(y_true, y_pred):
    """
    Display the confusion matrix with accuracy metric.
    """
    cm = confusion_matrix(y_true, y_pred)
    acc = accuracy_score(y_true, y_pred)

    fig, ax = plt.subplots(figsize=(4, 3))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No ICU", "ICU"])
    disp.plot(ax=ax, cmap='Greens', colorbar=False)
    ax.set_title(f"Confusion Matrix\nAccuracy: {acc*100:.2f}%")
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    plt.tight_layout()

    st.subheader("Confusion Matrix")
    st.pyplot(fig)
    st.metric(label="Accuracy", value=f"{acc*100:.2f}%")
