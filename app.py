# app.py

import gradio as gr
from modules.summarizer import summarize_text
from modules.classifier import classify_text
from modules.event_detector import detect_events

# Define individual task functions
def process_summarization(input_text):
    summary = summarize_text(input_text)
    return summary

def process_classification(input_text):
    classification = classify_text(input_text)
    return classification

def process_event_detection(input_text):
    events = detect_events(input_text)
    events_formatted = ', '.join(events) if isinstance(events, list) else events
    return events_formatted

# Create Gradio UI with Tabs
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # 🧠 NLP Assistant
        A simple app for:
        - 📚 Summarization
        - 🏷️ News Classification
        - 🗂️ Event Detection
        """
    )

    with gr.Tabs():
        # Summarization Tab
        with gr.Tab("📚 Summarization"):
            gr.Markdown(
                """
                ## 📚 Summarization
                Enter your text below and get a summarized version.

                ⚠️ **Note:**  
                - This task can take **~800–1000 seconds (~13–16 minutes)** for about **700–800 words**.  
                - Longer articles will take **even more time**.  
                - Please be patient!
                """
            )
            input_text_sum = gr.Textbox(
                label="Input Text for Summarization",
                placeholder="Paste your article, document, or paragraph here...",
                lines=10
            )
            summarize_btn = gr.Button("Summarize")
            summary_output = gr.Textbox(label="Summary", lines=8)

            summarize_btn.click(
                fn=process_summarization,
                inputs=[input_text_sum],
                outputs=[summary_output]
            )

        # Classification Tab
        with gr.Tab("🏷️ Classification"):
            gr.Markdown(
                """
                ## 🏷️ News/Text Classification
                Enter your text below to detect its category.
                """
            )
            input_text_classify = gr.Textbox(
                label="Input Text for Classification",
                placeholder="Paste your article or paragraph here...",
                lines=10
            )
            classify_btn = gr.Button("Classify")
            classification_output = gr.Textbox(label="Classification Result", lines=2)

            classify_btn.click(
                fn=process_classification,
                inputs=[input_text_classify],
                outputs=[classification_output]
            )

        # Event Detection Tab
        with gr.Tab("🗂️ Event Detection"):
            gr.Markdown(
                """
                ## 🗂️ Event Detection
                Extract keywords and named entities from your text.
                """
            )
            input_text_events = gr.Textbox(
                label="Input Text for Event Detection",
                placeholder="Paste your article, news, or report here...",
                lines=10
            )
            detect_btn = gr.Button("Detect Events")
            events_output = gr.Textbox(label="Detected Events", lines=8)

            detect_btn.click(
                fn=process_event_detection,
                inputs=[input_text_events],
                outputs=[events_output]
            )

# Launch Gradio app
if __name__ == "__main__":
    demo.launch()
