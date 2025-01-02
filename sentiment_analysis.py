
from transformers import pipeline
import streamlit as st

# Initialize pipelines
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.
    """
    result = sentiment_analyzer(text)
    return result[0]


