import pandas as pd
import streamlit as st
import joblib

#loading the model

model = joblib.load("diabetes_rf.pkl")


st.set_page_config(
    page_title="Diabetes Predictions",
    page_icon="🧬",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

/* Button */
div.stButton > button{
    width:100%;
    background:#1976D2;
    color:white;
    border-radius:10px;
    height:55px;
    font-size:20px;
    font-weight:bold;
}

div.stButton > button:hover{
    background:#1565C0;
    color:white;
}

/* Number input */
div[data-baseweb="input"]{
    border-radius:10px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#111827;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("🧬 Diabetes Prediction")

st.sidebar.info("""
This application predicts whether a patient is likely
to have diabetes based on health measurements.

Model Used:
Random Forest Classifier
""")

#Field Input
col1,col2 = st.columns(2)

with col1:

    Pregnancies = st.number_input("Pregnancies",0,20,2)

    Glucose = st.number_input("Glucose",0,300,85)

    BloodPressure = st.number_input("Blood Pressure",0,200,66)

    SkinThickness = st.number_input("Skin Thickness",0,100,20)

with col2:

    Insulin = st.number_input("Insulin",0,900,80)

    BMI = st.number_input("BMI",0.0,70.0,23.4)

    DiabetesPedigreeFunction = st.number_input(
        "Diabetes Pedigree Function",
        0.000,
        3.000,
        0.167,
        format="%.3f"
    )

    Age = st.number_input("Age",1,120,30)

#Prediction
if st.button("🔍 Predict Diabetes"):
    new_data= pd.DataFrame({
        "Pregnancies":[Pregnancies],
        "Glucose":[Glucose],
        "BloodPressure":[BloodPressure],
        "SkinThickness":[SkinThickness],
        "Insulin":[Insulin],
        "BMI":[BMI],
        "DiabetesPedigreeFunction":[DiabetesPedigreeFunction],
        "Age":[Age]
    })

    prediction = model.predict(new_data)
    probability = model.predict_proba(new_data)

    if prediction[0] == 1:
        st.error("🚨 High Risk of Diabetes")
        st.progress(int(probability[0][1] * 100))
        st.write(f"Confidence: **{probability[0][1] * 100:.2f}%**")
    else:
        st.success("✅ Low Risk of Diabetes")
        st.progress(int(probability[0][0] * 100))
        st.write(f"Confidence: **{probability[0][0] * 100:.2f}%**")

    st.markdown("---")
    st.subheader("📋 Patient Details")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Age", Age)
    col2.metric("BMI", BMI)
    col3.metric("Glucose", Glucose)
    col4.metric("Blood Pressure", BloodPressure)
