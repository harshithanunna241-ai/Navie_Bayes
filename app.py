import streamlit as st
import joblib

# Load trained model
model = joblib.load("naive_bayes_model.pkl")

# Title
st.title("Diabetes Prediction using Naive Bayes")

st.write("Enter the patient details below:")

# Input 1
glucose = st.number_input(
    "Glucose",
    min_value=0.0,
    max_value=500.0,
    value=100.0
)

# Input 2
bloodpressure = st.number_input(
    "Blood Pressure",
    min_value=0.0,
    max_value=300.0,
    value=80.0
)

# Prediction button
if st.button("Predict"):

    input_data = [[glucose, bloodpressure]]

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Prediction: Diabetes")
    else:
        st.success("Prediction: No Diabetes")