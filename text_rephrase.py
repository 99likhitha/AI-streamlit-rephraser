from transformers import pipeline

# Initialize text2text-generation pipeline for rephrasing
rephraser = pipeline("text2text-generation", model="facebook/bart-large-cnn")

def rephrase_text(text):
    """
    Rephrase the given text with improved clarity.
    """
    # Preprocess the text: Clean up and ensure proper formatting
    cleaned_text = " ".join(text.split())  # Remove redundant spaces

    # Use an explicit and clear prompt
    prompt = f"Paraphrase this text clearly and concisely: {cleaned_text}"

    # Rephrase using the model
    result = rephraser(prompt, max_length=150, do_sample=False)
    paraphrased_text = result[0]["generated_text"]

    paraphrased_text = paraphrased_text.replace(f"Paraphrase this text clearly and concisely: ", "").strip()
    # Post-process: Remove duplicates or incorrect phrasing
    final_text = " ".join(dict.fromkeys(paraphrased_text.split()))  # Remove repeated words
    return final_text


