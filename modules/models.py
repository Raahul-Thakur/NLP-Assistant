from transformers import pipeline
from keybert import KeyBERT
import torch

device = 0 if torch.cuda.is_available() else -1
print("Device set to:", "cuda" if device == 0 else "cpu")

summarizer = pipeline(
    "summarization",
    model="pszemraj/led-large-book-summary",
    tokenizer="pszemraj/led-large-book-summary",
    device=device
)

classifier = pipeline(
    "text-classification",
    model="ranudee/news-category-classifier",
    tokenizer="ranudee/news-category-classifier",
    device=device
)

kw_model = KeyBERT()
