
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Heart Disease Classification",
    page_icon="❤️",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load("heart_disease_model.joblib")

model = load_model()

st.title("❤️ Heart Disease Classification")
st.write(
    "An educational Machine Learning application "
    "using Logistic Regression."
)

st.warning(
    "Educational demo only. This model is not intended "
    "for medical diagnosis or treatment decisions."
)

st.subheader("Enter the Feature Values")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=50)
    sex = st.selectbox("Sex (0 or 1)", [0, 1])
    cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
    trestbps = st.number_input(
        "Resting Blood Pressure", min_value=0, value=120
    )
    chol = st.number_input(
        "Cholesterol", min_value=0, value=200
    )
    fbs = st.selectbox("Fasting Blood Sugar (fbs)", [0, 1])
    restecg = st.selectbox("Resting ECG (restecg)", [0, 1, 2])

with col2:
    thalach = st.number_input(
        "Maximum Heart Rate (thalach)", min_value=0, value=150
    )
    exang = st.selectbox("Exercise-Induced Angina (exang)", [0, 1])
    oldpeak = st.number_input(
        "Oldpeak", min_value=0.0, max_value=10.0,
        value=1.0, step=0.1
    )
    slope = st.selectbox("Slope", [0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3, 4])
    thal = st.selectbox("Thal", [0, 1, 2, 3])

if st.button("Run Prediction", type="primary"):
    input_data = pd.DataFrame([{
        "age": age,
        "sex": sex,
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }])

    prediction = model.predict(input_data)[0]

    st.subheader("Model Output")

    if prediction == 1:
        st.info("The model predicted class 1.")
    else:
        st.info("The model predicted class 0.")

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(input_data)[0]
        st.write("Model probability for each class:")
        st.write({
            "Class 0": f"{probabilities[0]:.2%}",
            "Class 1": f"{probabilities[1]:.2%}"
        })

