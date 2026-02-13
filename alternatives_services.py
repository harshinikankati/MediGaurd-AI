# services/alternatives_services.py

from utils.drug_data import DRUG_DATABASE

def get_alternatives(drug):
    """
    Return alternative medications for a given drug.

    Args:
        drug (str): Drug name.

    Returns:
        list: List of alternative drug names.
    """
    drug = drug.lower()

    return DRUG_DATABASE.get(
        drug,
        {}
    ).get(
        "alternatives",
        ["No alternatives available"]
    )
