import streamlit as st
import nltk
import pickle
import string
import os

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# ✅ Point to the correct NLTK data path
nltk.data.path.append(os.path.expanduser('~/.nltk_data'))

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)
