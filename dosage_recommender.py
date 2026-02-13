# services/dosage_recommender.py

from utils.drug_data import DRUG_DATABASE

def get_dosage(drug, age):
    drug = drug.lower()

    if drug not in DRUG_DATABASE:
        return "Dosage information not available"

    dosage_info = DRUG_DATABASE[drug].get("dosage", {})

    if age < 12:
        return dosage_info.get("child", "Consult pediatrician")
    elif age >= 65:
        return dosage_info.get(
            "elderly",
            dosage_info.get("adult", "Consult physician")
        )
    else:
        return dosage_info.get("adult", "Consult physician")



