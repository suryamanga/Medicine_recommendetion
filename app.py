import streamlit as st
import pandas as pd

from utils.predict import predict_disease
from utils.recommendation import recommend_medicine
# Load datasets
desc = pd.read_csv("data/symptom_Description.csv")
prec = pd.read_csv("data/symptom_precaution.csv")
import pickle

symptoms = pickle.load(open("model/symptoms.pkl", "rb"))

# UI
st.title("💊 Medicine Recommendation System")

selected = st.multiselect(
    "🤒 Select Your Symptoms",
    symptoms
)

if st.button("Predict"):
    disease = predict_disease(selected)
    
    st.success(f"Predicted Disease: {disease}")
    #
    
    # Description
    d = desc[desc['Disease'] == disease]['Description'].values
    if len(d) > 0:
        st.info(d[0])
    
     # Precautions
    p = prec[prec['Disease'] == disease].iloc[:,1:].values
    st.write("Precautions:")
    for item in p[0]:
        if str(item) != "nan":
            st.write("-", item)

    # ✅ ADD FROM HERE (medicine section)
    st.markdown("### 💊 Recommended Medicines")

    meds = recommend_medicine(disease)

    if len(meds) == 0:
        st.warning("No specific medicines found. Please consult a doctor.")
    else:
       for med in meds:
        st.write(f"💊 {med}")
import pickle

symptoms = pickle.load(open("model/symptoms.pkl", "rb"))