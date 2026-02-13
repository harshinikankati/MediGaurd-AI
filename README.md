# MediGaurd-AI
MediGuard AI is an AI-powered drug safety analysis system that uses NLP and speech recognition to extract medications from prescriptions, detect potential drug interactions, recommend age-specific dosages, and suggest alternative medications.

# 💊 MediGuard AI

MediGuard AI is an AI-powered drug safety analysis system that uses NLP
and speech recognition to extract medications from prescriptions,
detect potential drug interactions, recommend age-specific dosages,
and suggest alternative medications.

---

## 🚀 Features
- NLP-based drug extraction (Transformer models)
- Drug–drug interaction detection
- Age-specific dosage recommendations
- Alternative medication suggestions
- Speech-to-text prescription analysis
- Streamlit web interface

---

## 🧰 Tech Stack
- Python
- Streamlit
- HuggingFace Transformers
- Whisper ASR
- PyTorch

---

## 🗂 Data Coverage
Uses a curated dataset of commonly prescribed medications.
Designed to scale with real-world drug databases (RxNorm, OpenFDA).

---

## ⚠ Disclaimer
For educational and research purposes only.
Not intended for clinical use.

---

## ▶ How to Run
```bash
git clone https://github.com/yourusername/mediguard-ai
cd mediguard-ai
pip install -r requirements.txt
streamlit run app.py

