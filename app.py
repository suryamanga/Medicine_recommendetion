import streamlit as st
import pandas as pd
import pickle

from utils.predict import predict_disease
from utils.recommendation import recommend_medicine

# Page configuration
st.set_page_config(
    page_title="Medicine Recommendation System",
    page_icon="💊",
    layout="centered",
    initial_sidebar_state="auto"
)

# Load datasets
SYMPTOM_DESC = pd.read_csv("data/symptom_Description.csv")
SYMPTOM_PRECAUTION = pd.read_csv("data/symptom_precaution.csv")
symptoms = pickle.load(open("model/symptoms.pkl", "rb"))

# Header
st.title("💊 Medicine Recommendation System")
st.markdown(
    "This tool predicts a likely disease from selected symptoms and suggests precautions and medicines. "
    "Please select at least one symptom to get started."
)

# Selection area
selected = st.multiselect(
    "🤒 Select your symptoms",
    symptoms,
    help="Choose symptoms that best match how you feel"
)

if st.button("Predict"):
    if not selected:
        st.warning("Please select at least one symptom before predicting.")
    else:
        disease = predict_disease(selected)
        st.success(f"### Predicted Disease: {disease}")

        # Disease description
        description = SYMPTOM_DESC[SYMPTOM_DESC["Disease"] == disease]["Description"].values
        if len(description) > 0:
            st.info(description[0])

        # Precautions
        precautions = SYMPTOM_PRECAUTION[SYMPTOM_PRECAUTION["Disease"] == disease].iloc[:, 1:].values
        if precautions.size > 0:
            with st.expander("🧾 Precautions", expanded=True):
                for item in precautions[0]:
                    if str(item).strip().lower() != "nan" and str(item).strip():
                        st.write(f"- {item}")

        # Recommended medicines
        st.markdown("### 💊 Recommended Medicines")
        meds = recommend_medicine(disease)
        if len(meds) == 0:
            st.warning("No medicine recommendations found for this disease. Please consult a doctor.")
        else:
            for med in meds:
                st.write(f"- {med}")

     
