import streamlit as st
import torch

# ----------------------------
# Imports (NO DUPLICATES)
# ----------------------------
from models.text_model import load_text_model
from services.nlp_extractor import extract_drug_info
from services.interaction_checker import check_interactions
from services.dosage_recommender import get_dosage
from services.alternatives_services import get_alternatives
from utils.helpers import detect_drugs_in_text

# ----------------------------
# Load models (cached ONCE)
# ----------------------------
@st.cache_resource
def load_models():
    tokenizer, text_model, device = load_text_model()
    return tokenizer, text_model, device

tokenizer, text_model, DEVICE = load_models()

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("💊 AI Drug Safety & NLP Analysis System")

st.markdown("""
### Features
- Drug Interaction Detection  
- Age-Specific Dosage Recommendation  
- Alternative Medication Suggestions  
- NLP Drug Information Extraction
""")

# ----------------------------
# INPUT WIDGETS (DECLARED ONCE)
# ----------------------------
text = st.text_area(
    "Enter prescription or drug instructions:",
    key="prescription_input"
)

age = st.number_input(
    "Enter patient's age:",
    min_value=1,
    max_value=120,
    key="patient_age"
)

analyze_btn = st.button("Analyze", key="analyze_button")

# ----------------------------
# ANALYSIS LOGIC
# ----------------------------
if analyze_btn:
    if not text.strip():
        st.warning("Please enter prescription text.")
        st.stop()

    # 1️⃣ NLP extraction (TEXT OUTPUT)
    extracted_text = extract_drug_info(text, tokenizer, text_model)

    st.subheader("Raw NLP Output")
    st.code(extracted_text)

    # 2️⃣ Drug detection (RULE-BASED)
    drug_list = detect_drugs_in_text(text)

    st.subheader("Detected Drugs")
    st.write(drug_list if drug_list else "No drugs detected.")

    # 3️⃣ Drug interaction check
    interactions = check_interactions(drug_list)

    st.subheader("Drug Interaction Results")
    st.write(interactions if interactions else "No interactions detected.")

    # 4️⃣ Dosage + alternatives
    for drug in drug_list:
        st.markdown(f"### {drug.capitalize()}")
        st.write(f"**Dosage Recommendation:** {get_dosage(drug, age)}")
        st.write(f"**Alternatives:** {get_alternatives(drug)}")





