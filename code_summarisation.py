from transformers import pipeline

# Initialize summarization pipeline
summarizer = pipeline("summarization")

def summarize_code(code):
    """
    Summarize the given code.
    """
    prompt = f"Summarize the purpose and functionality of the following code:\n{code}"
    result = summarizer(prompt, max_length=150, min_length=30, do_sample=False)
    return result[0]["summary_text"]
