# All drug names MUST be lowercase

DOSAGES = {
    "metformin": {
        "adult": "500–2000 mg/day",
        "warning": "Monitor renal function"
    },
    "amlodipine": {
        "adult": "5–10 mg/day",
        "warning": "May cause edema"
    },
    "atorvastatin": {
        "adult": "10–80 mg/day",
        "warning": "Monitor liver enzymes"
    },
    "aspirin": {
        "adult": "75–325 mg/day",
        "warning": "Bleeding risk"
    }
}
# utils/drug_data.py

DRUG_DATABASE = {
    # 🩺 DIABETES
    "metformin": {
        "dosage": { "adult": "500–2000 mg/day", "child": "Not recommended" },
        "alternatives": ["glimepiride", "sitagliptin"],
        "interactions": ["cimetidine"]
    },
    "insulin": {
        "dosage": { "adult": "Individualized", "child": "Individualized" },
        "alternatives": ["metformin"],
        "interactions": ["beta blockers"]
    },

    # ❤️ CARDIOVASCULAR
    "amlodipine": {
        "dosage": { "adult": "5–10 mg/day", "child": "2.5–5 mg/day" },
        "alternatives": ["nifedipine"],
        "interactions": ["simvastatin"]
    },
    "atenolol": {
        "dosage": { "adult": "25–100 mg/day", "child": "1–2 mg/kg/day" },
        "alternatives": ["metoprolol"],
        "interactions": ["verapamil"]
    },
    "losartan": {
        "dosage": { "adult": "50–100 mg/day", "child": "0.7 mg/kg/day" },
        "alternatives": ["valsartan"],
        "interactions": ["lithium"]
    },

    # 🧠 CNS
    "paracetamol": {
        "dosage": { "adult": "500–4000 mg/day", "child": "10–15 mg/kg/dose" },
        "alternatives": ["ibuprofen"],
        "interactions": ["alcohol"]
    },
    "ibuprofen": {
        "dosage": { "adult": "1200–3200 mg/day", "child": "10 mg/kg/dose" },
        "alternatives": ["naproxen"],
        "interactions": ["aspirin"]
    },
    "aspirin": {
        "dosage": { "adult": "75–325 mg/day", "child": "Not recommended" },
        "alternatives": ["clopidogrel"],
        "interactions": ["warfarin"]
    },

    # 🦠 ANTIBIOTICS
    "amoxicillin": {
        "dosage": { "adult": "500 mg every 8 hrs", "child": "20–45 mg/kg/day" },
        "alternatives": ["cephalexin"],
        "interactions": ["methotrexate"]
    },
    "azithromycin": {
        "dosage": { "adult": "500 mg/day", "child": "10 mg/kg/day" },
        "alternatives": ["clarithromycin"],
        "interactions": ["warfarin"]
    },
    "ciprofloxacin": {
        "dosage": { "adult": "500 mg twice daily", "child": "Not recommended" },
        "alternatives": ["levofloxacin"],
        "interactions": ["theophylline"]
    },

    # 🧬 CHOLESTEROL
    "atorvastatin": {
        "dosage": { "adult": "10–80 mg/day", "child": "10–20 mg/day" },
        "alternatives": ["rosuvastatin"],
        "interactions": ["clarithromycin"]
    },
    "simvastatin": {
        "dosage": { "adult": "10–40 mg/day", "child": "10–20 mg/day" },
        "alternatives": ["pravastatin"],
        "interactions": ["amlodipine"]
    },

    # 🧠 PSYCHIATRIC
    "sertraline": {
        "dosage": { "adult": "50–200 mg/day", "child": "25–50 mg/day" },
        "alternatives": ["fluoxetine"],
        "interactions": ["mao inhibitors"]
    },
    "fluoxetine": {
        "dosage": { "adult": "20–80 mg/day", "child": "10–20 mg/day" },
        "alternatives": ["sertraline"],
        "interactions": ["tramadol"]
    },

    # 🌬 RESPIRATORY
    "salbutamol": {
        "dosage": { "adult": "2–4 mg 3x/day", "child": "1–2 mg" },
        "alternatives": ["terbutaline"],
        "interactions": ["beta blockers"]
    },

    # 🧂 GI
    "omeprazole": {
        "dosage": { "adult": "20–40 mg/day", "child": "10–20 mg/day" },
        "alternatives": ["pantoprazole"],
        "interactions": ["clopidogrel"]
    },
    "ranitidine": {
        "dosage": { "adult": "150 mg twice daily", "child": "2–4 mg/kg" },
        "alternatives": ["famotidine"],
        "interactions": ["ketoconazole"]
    }
}

# Total drugs here ≈ 120+ once expanded
