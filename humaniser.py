from transformers import pipeline

# Initialize text2text-generation pipeline for humanizing text
humanizer = pipeline("text2text-generation", model="t5-small")

def humanize_text(text):
    """
    Convert the given text into a more conversational tone.
    """
    prompt = f"Humanise these sentences: {text}"
    result = humanizer(prompt, max_length=150, do_sample=False)
    result=result.replace(f"Humanise these sentences:","").strip()
    return result[0]["generated_text"]
