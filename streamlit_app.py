import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('loan_status_model.joblib')

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f4f7f8;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #7f8c8d;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.image("https://img.freepik.com/free-vector/loan-application-abstract-concept-illustration_335657-3030.jpg", use_container_width=True)
st.markdown('<div class="title">🏦 Loan Approval Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Check if your loan can be approved with our smart AI model.</div>', unsafe_allow_html=True)
st.markdown("---")

# Main layout
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("🧍 Gender", ["Female (0)", "Male (1)"])
        married = st.selectbox("💑 Married", ["No (0)", "Yes (1)"])
        dependents = st.selectbox("🧒 Dependents", ["0", "1", "2", "3+", "4"])
        education = st.selectbox("📚 Education", ["Not Graduate (0)", "Graduate (1)"])
        self_employed = st.selectbox("💼 Self Employed", ["No (0)", "Yes (1)"])
        credit_history = st.selectbox("💳 Credit History", ["No (0.0)", "Yes (1.0)"])

    with col2:
        applicant_income = st.number_input("💰 Applicant Income", min_value=0.0)
        coapplicant_income = st.number_input("🤝 Coapplicant Income", min_value=0.0)
        loan_amount = st.number_input("🏦 Loan Amount", min_value=0.0)
        loan_amount_term = st.number_input("⏳ Loan Term (in days)", min_value=0.0)
        property_area = st.selectbox("📍 Property Area", ["Rural (0)", "Urban (1)", "Semiurban (2)"])

    # Convert display text to numeric values
    gender = 0 if gender.startswith("Female") else 1
    married = 0 if married.startswith("No") else 1
    dependents = 4 if dependents in ["4", "3+"] else int(dependents)
    education = 0 if education.startswith("Not") else 1
    self_employed = 0 if self_employed.startswith("No") else 1
    credit_history = 0.0 if credit_history.startswith("No") else 1.0
    property_area = {"Rural (0)": 0, "Urban (1)": 1, "Semiurban (2)": 2}[property_area]

    # Predict
    st.markdown("---")
    if st.button("🔍 Predict Loan Approval"):
        input_data = np.array([gender, married, dependents, education, self_employed,
                               applicant_income, coapplicant_income, loan_amount,
                               loan_amount_term, credit_history, property_area]).reshape(1, -1)

        prediction = model.predict(input_data)
        result = "✅ Approved" if prediction[0] == 1 else "❌ Rejected"

        st.markdown("### 📝 Result:")
        st.success(f"**Loan Status: {result}**")

    st.markdown('</div>', unsafe_allow_html=True)
