#!/bin/bash

# Optional: install missing spaCy model manually (if not auto-installed)
python -m spacy download en_core_web_md

# Start Streamlit app
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
