# app.py
import streamlit as st
from textblob import TextBlob

# Title
st.title("📝 Simple SpellChecker using TextBlob")

# Text input
input_text = st.text_area("Enter text to check spelling:", height=200)

# Button
if st.button("Check Spelling"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some text to check spelling.")
    else:
        corrected = str(TextBlob(input_text).correct())
        st.text_area("Corrected text:", corrected, height=200)
