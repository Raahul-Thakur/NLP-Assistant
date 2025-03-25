import streamlit as st
from modules.summarizer import summarize_text
from modules.classifier import classify_text
from modules.event_detector import detect_events
from modules.utils import read_pdf, fetch_article_from_url

st.set_page_config(page_title="NLP Assistant", layout="wide")
st.title("NLP Assistant - Summarization, Classification & Event Detection")

tab1, tab2, tab3 = st.tabs(["Summarization", "News Classification", "Event Detection"])

with tab1:
    st.subheader("Summarize Text, PDF, or URL")
    text_input = st.text_area("Paste Article", height=300)
    pdf_input = st.file_uploader("Upload PDF", type="pdf")
    url_input = st.text_input("Paste Article URL")

    if st.button("Summarize"):
        if url_input.strip():
            content = fetch_article_from_url(url_input)
        elif pdf_input:
            content = read_pdf(pdf_input)
        else:
            content = text_input

        with st.spinner("Summarizing..."):
            st.text_area("Summary", summarize_text(content), height=400)

with tab2:
    st.subheader("Classify News Content")
    classify_input = st.text_area("Enter News Content", height=300)
    if st.button("Classify"):
        with st.spinner("Classifying..."):
            st.success(classify_text(classify_input))

with tab3:
    st.subheader("Detect Key Events from Text")
    event_input = st.text_area("Enter Article or Paragraph", height=300)
    if st.button("Detect Events"):
        with st.spinner("Detecting..."):
            st.success(detect_events(event_input))
