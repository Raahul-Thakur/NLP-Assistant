from keybert import KeyBERT
import spacy
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

kw_model = KeyBERT()
nlp = spacy.load("en_core_web_md")

def get_top_keywords(text, top_n=5):
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english')
    
    seen = set()
    deduped_keywords = []
    
    for word, _ in keywords:
        simplified = word.lower().replace("-", " ").replace("_", " ")
        if simplified not in seen:
            seen.add(simplified)
            deduped_keywords.append(word)
        if len(deduped_keywords) >= top_n:
            break

    return deduped_keywords

def get_top_named_entities(text, top_n=15):
    doc = nlp(text)
    entities = [ent.text.strip() for ent in doc.ents if ent.label_ in {"PERSON", "ORG", "GPE", "EVENT", "PRODUCT", "LOC", "FAC"}]

    counter = Counter(entities)
    ranked_entities = [entity for entity, _ in counter.most_common(top_n)]
    
    return ranked_entities

def detect_events(text):
    keywords = get_top_keywords(text)
    named_entities = get_top_named_entities(text)
    
    return {
        "Top Keywords (KeyBERT)": keywords,
        "Top Named Entities (NER)": named_entities
    }
