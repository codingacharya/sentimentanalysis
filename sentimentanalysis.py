import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER lexicon
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Streamlit App
st.title("Sentiment Analysis App")
st.write("Enter a text to analyze its sentiment.")

# User Input
user_input = st.text_area("Enter your text here:")

if st.button("Analyze Sentiment"):
    if user_input:
        sentiment_score = sia.polarity_scores(user_input)
        compound_score = sentiment_score['compound']

        # Determine sentiment category
        if compound_score >= 0.05:
            sentiment = "Positive 😊"
        elif compound_score <= -0.05:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"
        
        # Display results
        st.subheader("Sentiment Analysis Result")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Scores:** {sentiment_score}")
    else:
        st.warning("Please enter some text to analyze.")
