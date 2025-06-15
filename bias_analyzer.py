from newspaper import Article
import requests
import re
from transformers import pipeline
import streamlit as st

# UI
st.title("Political Bias Detector")

# NLP object
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Extract Article object from valid URL
def getURl() -> Article:
    articleURL = st.text_input("Paste your article's URL: ")
    notGot = True
    while(notGot):
        try:
            requests.get(articleURL)
            notGot = False
        except:
            articleURL = st.text_input("Invalid URL, try again: ")
            notGot = True
    return Article(articleURL)

# Get main text body
def getText(a : Article):
    a.download()
    a.parse()
    return a.text

# Clean text
def clean(txt : str) -> str:
    re.sub(r'/s+', ' ', txt)
    re.sub(r'[^\w\s]', '', txt)
    return txt.lower()


