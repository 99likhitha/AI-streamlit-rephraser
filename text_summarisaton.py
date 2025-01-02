from transformers import pipeline

# Initialize summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    """
    Summarize the given text.
    """
    result = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return result[0]["summary_text"]
