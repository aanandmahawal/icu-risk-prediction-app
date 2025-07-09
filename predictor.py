import pandas as pd
import streamlit as st
from utils import explain_risk_factors

def streamlit_predict_custom_input(clf):
    st.subheader("🧾 Enter Patient Vitals")

    HR = st.number_input("💓 Heart Rate (bpm)", value=80)
    BP = st.number_input("🩸 Blood Pressure (mmHg)", value=120)
    Temp = st.number_input("🌡️ Body Temperature (°F)", value=98.6)
    RespRate = st.number_input("🫁 Respiratory Rate (breaths/min)", value=18)
    ComorbidityIndex = st.slider("📊 Comorbidity Index", 0, 5, value=2)

    if st.button("🚨 Predict ICU Risk"):
        input_df = pd.DataFrame([{
            'HR': HR,
            'BP': BP,
            'Temp': Temp,
            'RespRate': RespRate,
            'ComorbidityIndex': ComorbidityIndex
        }])

        # 🚨 ICU risk override for extreme values
        force_icu = (
            HR < 50 or HR > 130 or
            BP < 80 or BP > 180 or
            Temp < 94 or Temp > 105 or
            RespRate < 10 or RespRate > 30 or
            ComorbidityIndex > 3
        )

        with st.spinner("🔎 Predicting..."):
            try:
                if force_icu:
                    prediction = 1
                    prob = 1.0
                else:
                    prediction = clf.predict(input_df.to_numpy())[0]
                    try:
                        prob = clf.predict_proba(input_df.to_numpy())[0][1]
                    except:
                        prob = None

                if prediction == 1:
                    st.error("🛑 Prediction: ICU Risk")
                else:
                    st.success("✅ Prediction: No ICU Risk")

                if prob is not None:
                    st.info(f"📈 ICU Risk Probability: **{prob:.2%}**")

                explain_risk_factors(input_df, prediction, streamlit_mode=True)

            except Exception as e:
                st.error(f"Prediction failed: {str(e)}")
