#!/bin/bash

# Ensure the PORT Render expects is used
export PORT=${PORT:-8501}

# Run Streamlit binding to the correct host and port
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0