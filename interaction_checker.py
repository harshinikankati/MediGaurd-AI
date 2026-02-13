# services/interaction_checker.py

from utils.drug_data import DRUG_DATABASE

def check_interactions(drug_list):
    """
    Check for interactions between a list of drugs.

    Parameters:
        drug_list (list of str): List of detected drug names.

    Returns:
        list of str: Interaction warnings.
    """
    interactions = []
    drugs = [drug.lower() for drug in drug_list]

    for drug in drugs:
        interaction_list = DRUG_DATABASE.get(drug, {}).get("interactions", [])

        for interacting_drug in interaction_list:
            if interacting_drug in drugs:
                interactions.append(
                    f"⚠ Interaction detected between {drug} and {interacting_drug}"
                )

    return list(set(interactions))



