# app.py

import streamlit as st
import numpy as np
import pickle
import os

# -----------------------------
# Load model and scaler
# -----------------------------
if os.path.exists("model.pkl") and os.path.exists("scaler.pkl"):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
else:
    st.error("❌ Model or Scaler file not found! Make sure 'model.pkl' and 'scaler.pkl' are in the same folder as this app.")
    st.stop()

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Heart Failure Prediction", page_icon="🫀", layout="centered")
st.title("🫀 Heart Failure Prediction System")
st.write("Enter your health information below to predict your risk of heart failure. No medical expertise needed!")

# -----------------------------
# User-friendly input fields
# -----------------------------
age = st.number_input("Age (years)", min_value=1, max_value=120, value=60)

anaemia = st.selectbox("Do you have anemia?", ["No", "Yes"])

creatinine_phosphokinase = st.number_input(
    "Blood Enzyme Level (CPK)", min_value=1, max_value=10000, value=300,
    help="This is a blood enzyme level; just enter the number from your lab test if available."
)

diabetes = st.selectbox("Do you have diabetes?", ["No", "Yes"])

ejection_fraction = st.number_input(
    "Heart Pump Efficiency (%)", min_value=10, max_value=90, value=50,
    help="Percentage of blood pumped by your heart each beat."
)

high_blood_pressure = st.selectbox("Do you have high blood pressure?", ["No", "Yes"])

# Platelets in thousands for user-friendliness
platelets_input = st.number_input(
    "Platelet Count (thousands/mL)", min_value=10, max_value=1000, value=250,
    help="Enter the platelet count in thousands (e.g., 250 means 250,000)"
)
platelets = platelets_input * 1000  # convert to actual count for model

serum_creatinine = st.number_input(
    "Kidney Function Level (Creatinine mg/dL)", min_value=0.1, max_value=10.0, step=0.1, value=1.0
)

serum_sodium = st.number_input("Blood Sodium Level (mEq/L)", min_value=100, max_value=160, value=135)

sex = st.selectbox("Sex", ["Female", "Male"])

smoking = st.selectbox("Do you smoke?", ["No", "Yes"])

# -----------------------------
# Convert categorical fields to numeric
# -----------------------------
anaemia = 1 if anaemia == "Yes" else 0
diabetes = 1 if diabetes == "Yes" else 0
high_blood_pressure = 1 if high_blood_pressure == "Yes" else 0
sex = 1 if sex == "Male" else 0
smoking = 1 if smoking == "Yes" else 0

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Heart Failure"):
    input_data = np.array([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                            high_blood_pressure, platelets, serum_creatinine, serum_sodium,
                            sex, smoking]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Failure. Consult a doctor immediately!")
    else:
        st.success("✅ Low Risk of Heart Failure. Stay healthy!")

# -----------------------------
# Team Credits
# -----------------------------
st.markdown("---")
st.subheader("👥 Team Credits")
st.write("""
- Albert Antony S  
- Jeevanesh K
- Elaichandiran S
- Kumaran M
""")

