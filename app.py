import streamlit as st
import nltk
import os
import pickle
import string

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# ✅ 1) Set up local nltk_data directory
nltk_data_dir = os.path.join(os.path.dirname(__file__), "nltk_data")
nltk.data.path.append(nltk_data_dir)

# ✅ 2) Download punkt tokenizer if not present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', download_dir=nltk_data_dir)

# ✅ 3) Download stopwords too (optional, but needed!)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', download_dir=nltk_data_dir)

# ✅ 4) Initialize stemmer
ps = PorterStemmer()

# ✅ 5) Preprocessing function
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

# ✅ 6) Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# ✅ 7) Streamlit UI
st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # 1. Preprocess
    transformed_sms = transform_text(input_sms)
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. Predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
