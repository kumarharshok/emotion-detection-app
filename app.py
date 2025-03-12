import streamlit as st
import joblib
import pandas as pd

# Load the trained model and vectorizer
model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Title of the web app
st.title("😊 Emotion Detection App 🎭")
st.markdown("### Enter a sentence and find out the emotion!")

# User input
user_input = st.text_area("Enter your text here:", "")

if st.button("Detect Emotion"):
    if user_input:
        # Transform input text
        input_tfidf = vectorizer.transform([user_input])
        
        # Predict Emotion
        prediction = model.predict(input_tfidf)[0]
        
        # Define emotion labels
        emotions = {
            0: "Sadness 😢",
            1: "Joy 😃",
            2: "Love ❤️",
            3: "Anger 😡",
            4: "Fear 😨",
            5: "Surprise 😲"
        }
        
        # Show Prediction
        st.success(f"**Predicted Emotion:** {emotions[prediction]}")
    else:
        st.warning("Please enter some text before clicking 'Detect Emotion'.")
