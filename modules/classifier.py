from .models import classifier

label_map = {
    "LABEL_0": "Business",
    "LABEL_1": "Entertainment",
    "LABEL_2": "Health",
    "LABEL_3": "Science",
    "LABEL_4": "Sports",
    "LABEL_5": "Technology",
    "LABEL_6": "Politics",
    "LABEL_7": "World"
}

def classify_text(text):
    chunk_size = 1024
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    label_scores = {}

    for i, chunk in enumerate(chunks):
        try:
            results = classifier(chunk)
            for res in results:
                label = res['label']
                score = res['score']
                label_scores[label] = label_scores.get(label, 0) + score
        except Exception as e:
            print(f"⚠️ Error classifying chunk {i+1}: {e}")
            continue

    if not label_scores:
        return "⚠️ Could not classify any chunk."

    final_label = max(label_scores, key=label_scores.get)
    confidence = round(label_scores[final_label] / len(chunks), 3)
    readable_label = label_map.get(final_label, final_label)
    return f"{readable_label.upper()} (Aggregated Score: {confidence})"
