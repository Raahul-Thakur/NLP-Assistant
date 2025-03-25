from .models import summarizer

def summarize_text(text):
    chunk_size = 3000
    overlap = 200
    summaries = []

    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size - overlap)]
    for i, chunk in enumerate(chunks):
        try:
            summary = summarizer(chunk, min_length=50, max_length=256, truncation=True)[0]['summary_text']
            summaries.append(f"\n Chunk {i+1} Summary:\n{summary}")
        except Exception as e:
            summaries.append(f"Error in chunk {i+1}: {e}")

    try:
        meta_input = " ".join([s.split("\n", 1)[-1] for s in summaries])
        final = summarizer(meta_input, min_length=50, max_length=256, truncation=True)[0]['summary_text']
        summaries.append(f"\nFinal Meta-Summary:\n{final}")
    except Exception as e:
        summaries.append(f"Error in meta-summary: {e}")

    return "\n".join(summaries)
