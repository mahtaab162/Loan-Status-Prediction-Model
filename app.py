import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("LoanStatusPrediction.pkl", "rb"))

# Streamlit page config
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="centered"
)

# Title
st.title("🏦 Loan Approval Prediction App")

st.write("Fill all details below to predict loan approval status.")

# USER INPUTS

no_of_dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    max_value=10,
    step=1
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

income_annum = st.number_input(
    "Annual Income",
    min_value=0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0
)

loan_term = st.number_input(
    "Loan Term",
    min_value=0
)

cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900
)

residential_assets_value = st.number_input(
    "Residential Assets Value",
    min_value=0
)

commercial_assets_value = st.number_input(
    "Commercial Assets Value",
    min_value=0
)

luxury_assets_value = st.number_input(
    "Luxury Assets Value",
    min_value=0
)

bank_asset_value = st.number_input(
    "Bank Asset Value",
    min_value=0
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

# ENCODING

# self_employed encoding
if self_employed == "Yes":
    self_employed = 1
else:
    self_employed = 0

# education one-hot encoding
if education == "Graduate":
    education_Graduate = 1
    education_Not_Graduate = 0
else:
    education_Graduate = 0
    education_Not_Graduate = 1

# PREDICTION

if st.button("Predict Loan Status"):

    # Create dataframe with EXACT feature order
    input_data = pd.DataFrame([[
        no_of_dependents,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value,
        education_Graduate,
        education_Not_Graduate
    ]], columns=[
        'no_of_dependents',
        'self_employed',
        'income_annum',
        'loan_amount',
        'loan_term',
        'cibil_score',
        'residential_assets_value',
        'commercial_assets_value',
        'luxury_assets_value',
        'bank_asset_value',
        'education_Graduate',
        'education_Not Graduate'
    ])

    # Prediction
    prediction = model.predict(input_data)

    # Output
    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")