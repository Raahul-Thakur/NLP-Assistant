# 🤖 NLP Assistant

A lightweight NLP-powered assistant that provides **summarization**, **news classification**, and **event detection** from text, PDF uploads, or article URLs. Built using `Transformers`, `KeyBERT`, `Streamlit`, and `pdfplumber`.

---

## 🚀 Features

- 📄 **Summarization** (with sliding window + meta-summary)
- 🗞️ **News Classification** using `DistilBERT`
- 📌 **Event Detection** with `KeyBERT`, `spaCy` & `TF-IDF`
- 📥 Upload **PDFs**
- 🔗 Input article **URLs** using `newspaper3k`

---

## 🛠️ Tech Stack

- `Streamlit` - Web UI
- `Transformers` (HuggingFace)
- `KeyBERT`
- `pdfplumber` for PDF extraction
- `PyTorch` (auto GPU/CPU)
- `scikit-learn` & `sentence-transformers` for KeyBERT
- `newspaper3k` for url support
- `spacy` & `TfidfVectorizer` for Extracting NER

---

## 📁 Folder Structure

nlp_assistant/ ├── app.py # Main Streamlit app ├── requirements.txt # Python dependencies ├── README.md # Project documentation ├── assets/ # Optional test PDFs │ └── sample.pdf └── modules/ # Modularized logic ├── init.py ├── classifier.py # News classification ├── event_detector.py # Event detection ├── models.py # Model loading ├── summarizer.py # Summarization └── utils.py # PDF reader


---

## 🧑‍💻 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Raahul-Thakur/NLP-Assistant.git
cd NLP-ASSISTANT
```

### 2. Requirements

pip install -r requirements.txt

### 3. Run the app

streamlit run app.py


Models Used
Task	            Model
Summarization	pszemraj/led-large-book-summary (Long LED Transformer)
Classification	
Event Detection	     KeyBERT with sentence-transformers

---

Let me know if you’d like to:

- Add badges (stars, forks, license)
- Include a demo GIF/screenshot
- contact
  
LinkedIn: https://www.linkedin.com/in/rahul-t-171458190/
Instagram: https://www.instagram.com/rah.ipynb
Gmail: raahul.thakurr01@gmail.com

Deployment
https://nlp-assistant.streamlit.app/
