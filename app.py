# import streamlit as st
# from CodeAnalysis import analyze_code_transformer
# from CodeBugFound import analyze_code
# from CodeSummarizer_Debugger import analyze_code_summarise
# from D16_NLPTasks_Transformers import summarization_task, sentiment_analysis_task, rephrasing_task

# # App Title
# st.title("NLP and Code Analysis Toolkit")

# # Sidebar for navigation
# st.sidebar.title("Select a Task")
# task = st.sidebar.selectbox("Choose a functionality:", [
#     "Code Analysis",
#     "Bug Detection",
#     "Code Summarization and Debugging",
#     "Text Summarization",
#     "Sentiment Analysis",
#     "Text Rephrasing"
# ])

# # Task-specific logic
# if task == "Code Analysis":
#     st.header("Code Analysis")
#     code = st.text_area("Paste your code here:")
#     if st.button("Analyze Code"):
#         result = analyze_code_transformer(code)
#         st.write(result)

# elif task == "Bug Detection":
#     st.header("Bug Detection and Code Formatting")
#     code = st.text_area("Paste your code here:")
#     lang = st.selectbox("Select Language:", ["Python", "JavaScript"])
#     if st.button("Detect Bugs"):
#         result = analyze_code(code, lang)
#         st.code(result)

# elif task == "Code Summarization and Debugging":
#     st.header("Code Summarization and Debugging")
#     code = st.text_area("Paste your code here:")
#     if st.button("Summarize and Debug"):
#         summary, debug_info = analyze_code_summarise(code)
#         st.subheader("Code Summary")
#         st.write(summary)
#         st.subheader("Debugging Info")
#         st.write(debug_info)

# elif task == "Text Summarization":
#     st.header("Text Summarization")
#     text = st.text_area("Enter text to summarize:")
#     if st.button("Summarize Text"):
#         summary = summarization_task(text)
#         st.write(summary)

# elif task == "Sentiment Analysis":
#     st.header("Sentiment Analysis")
#     text = st.text_area("Enter text to analyze sentiment:")
#     if st.button("Analyze Sentiment"):
#         sentiment = sentiment_analysis_task(text)
#         st.write(sentiment)

# elif task == "Text Rephrasing":
#     st.header("Text Rephrasing")
#     text = st.text_area("Enter text to rephrase:")
#     if st.button("Rephrase Text"):
#         rephrased_text = rephrasing_task(text)
#         st.write(rephrased_text)


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
