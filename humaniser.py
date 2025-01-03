from transformers import pipeline

# # Initialize text2text-generation pipeline for humanizing text
humanizer = pipeline("text2text-generation", model="facebook/bart-large-cnn")


# def humanize_text(text):
#     """
#     Convert the given text into a more conversational tone.
#     """
#     prompt = f"Humanise these sentences: {text}"
#     result = humanizer(prompt, max_length=150, do_sample=False)
#     result=result[0]["generated_text"]
#     result=result.replace(f"Humanise these sentences:","").strip()
#     return result

def humanize_text(text):
    """
    Rephrase the given text with a more natural, conversational tone.
    """
    # Preprocess the text: Clean up and ensure proper formatting
    cleaned_text = " ".join(text.split())  # Remove redundant spaces

    # Modify the prompt to encourage a more human-like rephrasing
    prompt = f"Explain this text in a way that’s easy to understand: {cleaned_text}"

    # Rephrase using the model
    result = humanizer(prompt, max_length=150, do_sample=False)
    paraphrased_text = result[0]["generated_text"]

    # Remove the prompt phrase from the output text
    final_text = paraphrased_text.replace(f"Explain this text in a way that’s easy to understand:", "").strip()

    # Post-process: Remove duplicates or incorrect phrasing
    final_text = " ".join(dict.fromkeys(final_text.split()))  # Remove repeated words
    return final_text
