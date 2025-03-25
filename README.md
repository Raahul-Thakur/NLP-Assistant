# 🤖 NLP Assistant

A lightweight NLP-powered assistant that provides **summarization**, **news classification**, and **event detection** from text, PDF uploads, or article URLs. Built using `Transformers`, `KeyBERT`, `Streamlit`, and `pdfplumber`.

---

## 🚀 Features

- 📄 **Summarization** (with sliding window + meta-summary)
- 🗞️ **News Classification** using `DistilBERT`
- 📌 **Event Detection** with `KeyBERT`
- 📥 Upload **PDFs**
- 🔗 Input article **URLs** *(planned for next update)*

---

## 🛠️ Tech Stack

- `Streamlit` - Web UI
- `Transformers` (HuggingFace)
- `KeyBERT`
- `pdfplumber` for PDF extraction
- `PyTorch` (auto GPU/CPU)
- `scikit-learn` & `sentence-transformers` for KeyBERT

---

## 📁 Folder Structure

nlp_assistant/ ├── app.py # Main Streamlit app ├── requirements.txt # Python dependencies ├── README.md # Project documentation ├── assets/ # Optional test PDFs │ └── sample.pdf └── modules/ # Modularized logic ├── init.py ├── classifier.py # News classification ├── event_detector.py # Event detection ├── models.py # Model loading ├── summarizer.py # Summarization └── utils.py # PDF reader


---

## 🧑‍💻 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Raahul-Thakur/nlp-assistant.git
cd nlp-assistant
```

### 2. Requirements

pip install -r requirements.txt

### 3. Run the app

streamlit run app.py


Models Used
Task	            Model
Summarization	pszemraj/led-large-book-summary (Long LED Transformer)
Classification	Yueh-Huan/news-category-classification-distilbert
Event Detection	     KeyBERT with sentence-transformers

---

Let me know if you’d like to:

- Add badges (stars, forks, license)
- Include a demo GIF/screenshot
- Change the contact link or name

Want me to add this `README.md` directly to your folder via the canvas?