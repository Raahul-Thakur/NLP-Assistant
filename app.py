# app.py

import gradio as gr
from modules.summarizer import summarize_text
from modules.classifier import classify_text
from modules.event_detector import detect_events

# Main function that processes input
def process_text(input_text):
    summary = summarize_text(input_text)
    classification = classify_text(input_text)
    events = detect_events(input_text)
    
    # Display events in a comma-separated format
    events_formatted = ', '.join(events) if isinstance(events, list) else events
    return summary, classification, events_formatted

# Create the Gradio UI
with gr.Blocks() as demo:
    gr.Markdown(
        """
        # 🧠 NLP Assistant
        Enter your text below and get:
        - 📚 **Summarization**
        - 🏷️ **Text Classification**
        - 🗂️ **Event Detection**
        """
    )

    with gr.Row():
        input_text = gr.Textbox(
            label="Input Text",
            placeholder="Paste your article, document, or paragraph here...",
            lines=10
        )

    with gr.Row():
        submit_btn = gr.Button("Process")

    with gr.Row():
        summary_output = gr.Textbox(label="Summary", lines=5)
        classification_output = gr.Textbox(label="Classification", lines=2)
        events_output = gr.Textbox(label="Detected Events", lines=5)

    submit_btn.click(
        fn=process_text,
        inputs=[input_text],
        outputs=[summary_output, classification_output, events_output]
    )

# Launch Gradio app
if __name__ == "__main__":
    demo.launch()
