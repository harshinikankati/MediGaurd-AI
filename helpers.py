# utils/helpers.py

import re
from utils.drug_data import DRUG_DATABASE

def detect_drugs_in_text(text):
    """
    Detect drug names mentioned in free-text input.

    Args:
        text (str): Input text (e.g., prescription or notes)

    Returns:
        list: List of detected drug names
    """
    if not text:
        return []

    # Normalize text
    clean_text = re.sub(r"[^\w\s]", "", text.lower())
    words = set(clean_text.split())

    detected_drugs = [
        drug for drug in DRUG_DATABASE.keys()
        if drug in words
    ]

    return detected_drugs
