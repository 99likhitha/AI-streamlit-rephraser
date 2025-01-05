import streamlit as st
from code_summarisation import summarize_code
from text_summarisaton import summarize_text
from sentiment_analysis import analyze_sentiment
from text_rephrase import rephrase_text
from humaniser import humanize_text

st.title("NLP Toolkit")

# Sidebar for navigation
task = st.sidebar.selectbox("Choose a task:", [
    "Code Summarisation",
    "Text Summarisation",
    "Sentiment Analysis",
    "Text Rephrasing",
    "Humanise Text"
])

if task == "Code Summarisation":
    st.header("Code Summarisation")
    code = st.text_area("Enter code to summarise:")
    if st.button("Summarise Code"):
        summary = summarize_code(code)
        st.write(summary)

elif task == "Text Summarisation":
    st.header("Text Summarisation")
    text = st.text_area("Enter text to summarise:")
    if st.button("Summarise Text"):
        summary = summarize_text(text)
        st.write(summary)

elif task == "Sentiment Analysis":
    st.header("Sentiment Analysis")
    text = st.text_area("Enter text to analyse sentiment:")
    # if st.button("Analyze Sentiment"):
    #     sentiment = analyze_sentiment(text)
    #     st.write(sentiment)
    if st.button("Analyze Sentiment"):
        if not text.strip():  # Check if the input is empty or contains only whitespace
            st.warning("Please enter some text for sentiment analysis. Empty strings are not allowed!")
        else:
            # Perform sentiment analysis
            result = analyze_sentiment(text)
            st.write(f"**Sentiment:** {result['label']} ({result['score'] * 100:.2f}% confidence)")

elif task == "Text Rephrasing":
    st.header("Text Rephrasing")
    text = st.text_area("Enter text to rephrase:")
    if st.button("Rephrase Text"):
        rephrased_text = rephrase_text(text)
        st.write(rephrased_text)

elif task == "Humanise Text":
    st.header("Humanise Text")
    text = st.text_area("Enter text to humanise:")
    if st.button("Humanise Text"):
        humanised_text = humanize_text(text)
        st.write(humanised_text)
