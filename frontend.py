import streamlit as st
import requests

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure (months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges")

if st.button("Predict"):
    url = "http://127.0.0.1:8000/predict"

    data = {
        "tenure": int(tenure),
        "monthly_charges": float(monthly_charges)
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['result']}")
    else:
        st.error("Error connecting to API")
