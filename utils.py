def explain_risk_factors(input_df, prediction, streamlit_mode=False):
    hr = input_df['HR'].iloc[0]
    bp = input_df['BP'].iloc[0]
    rr = input_df['RespRate'].iloc[0]
    ci = input_df['ComorbidityIndex'].iloc[0]
    temp = input_df['Temp'].iloc[0]

    reasons = []

    # Heart Rate
    if hr < 60:
        reasons.append(f"🔻 Low Heart Rate: {hr} bpm (below 60)")
    elif hr > 100:
        reasons.append(f"🔺 High Heart Rate: {hr} bpm (above 100)")

    # Blood Pressure
    if bp < 90:
        reasons.append(f"🔻 Low Blood Pressure: {bp} mmHg (below 90)")
    elif bp > 140:
        reasons.append(f"🔺 High Blood Pressure: {bp} mmHg (above 140)")

    # Respiratory Rate
    if rr < 12:
        reasons.append(f"🔻 Low Respiratory Rate: {rr} breaths/min (below 12)")
    elif rr > 20:
        reasons.append(f"🔺 High Respiratory Rate: {rr} breaths/min (above 20)")

    # Temperature
    if temp < 95:
        reasons.append(f"❄️ Low Body Temperature: {temp}°F (below 95)")
    elif temp > 100.4:
        reasons.append(f"🌡️ High Body Temperature: {temp}°F (above 100.4)")

    # Comorbidity Index
    if ci < 1:
        reasons.append(f"🔻 Low Comorbidity Index: {ci} (below 1 — may indicate missing data)")
    elif ci > 2:
        reasons.append(f"⚠️ High Comorbidity Index: {ci} (above 2)")

    # Output function
    def out(msg, is_header=False):
        if streamlit_mode:
            import streamlit as st
            if is_header:
                st.markdown(f"### {msg}")
            else:
                st.markdown(msg)
        else:
            print(msg)

    # Explanation output
    out("Explanation of Risk Factors:", is_header=True)

    if prediction == 1:
        if reasons:
            out("🛑 ICU likely required due to:")
            for r in reasons:
                out(f"- {r}")
        else:
            out("🛑 ICU risk predicted, but no strong individual vital signs triggered.")
    else:
        if reasons:
            out("⚠️ Some warning signs detected, but overall patient is not classified as ICU risk:")
            for r in reasons:
                out(f"- {r}")
        else:
            out("✅ All vital signs are within safe clinical range.")
