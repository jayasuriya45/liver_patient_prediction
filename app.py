import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("logistic_liver_model.pkl")

st.title("Liver Disease Prediction")

st.write("Enter patient details")

# User inputs
age = st.number_input("Age")
gender = st.selectbox("Gender", ["Male", "Female"])
total_bilirubin = st.number_input("Total Bilirubin")
direct_bilirubin = st.number_input("Direct Bilirubin")
alkaline_phosphotase = st.number_input("Alkaline Phosphotase")
alamine_aminotransferase = st.number_input("Alamine Aminotransferase")
aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase")
total_proteins = st.number_input("Total Proteins")
albumin = st.number_input("Albumin")
albumin_globulin_ratio = st.number_input("Albumin Globulin Ratio")

# Convert gender
gender = 1 if gender == "Male" else 0

# Prediction button
if st.button("Predict"):

    input_data = np.array([[age, gender, total_bilirubin, direct_bilirubin,
                            alkaline_phosphotase, alamine_aminotransferase,
                            aspartate_aminotransferase, total_proteins,
                            albumin, albumin_globulin_ratio]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Liver Disease Detected")
    else:
        st.success("✅ No Liver Disease")