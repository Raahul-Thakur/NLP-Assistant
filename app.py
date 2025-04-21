# app.py
from flask import Flask, request, render_template
from modules.summarizer import summarize_text
from modules.classifier import classify_text
from modules.event_detector import detect_events
from modules.utils import read_pdf, fetch_article_from_url

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/summarize', methods=['POST'])
def summarize():
    content = ""
    if 'url_input' in request.form and request.form['url_input'].strip():
        content = fetch_article_from_url(request.form['url_input'])
    elif 'pdf_input' in request.files and request.files['pdf_input'].filename:
        pdf_file = request.files['pdf_input']
        content = read_pdf(pdf_file)
    else:
        content = request.form.get('text_input', '')

    summary = summarize_text(content)
    return render_template("index.html", summary=summary)

@app.route('/classify', methods=['POST'])
def classify():
    text = request.form.get('classify_input', '')
    classification = classify_text(text)
    return render_template("index.html", classification=classification)

@app.route('/events', methods=['POST'])
def events():
    text = request.form.get('event_input', '')
    events = detect_events(text)
    return render_template("index.html", events=events)

if __name__ == '__main__':
    app.run(debug=True, port=10000, host='0.0.0.0')
