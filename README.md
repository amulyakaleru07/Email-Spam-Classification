# Email-Spam-Classification

This project aims to classify emails as **Spam** or **Ham** (Not Spam) using Natural Language Processing (NLP) and a Logistic Regression machine learning model.

## 🚀 Project Overview

Unwanted spam emails are a common problem, filling up inboxes with irrelevant or harmful content. This project demonstrates how to build a simple spam filter using Python, NLP techniques, and supervised machine learning. The final result is a web app where users can input any email text and instantly check if it’s likely to be spam.

## 🧩 How It Works

The project follows these main steps:

### 1️⃣ Data Collection
A dataset containing a large number of emails labeled as **spam** or **ham** is used for training and testing the model.

### 2️⃣ Text Preprocessing
Raw email text is cleaned and prepared using Natural Language Processing techniques:
- **Lowercasing:** Converts all text to lowercase to avoid treating the same word differently.
- **Tokenization:** Splits text into individual words.
- **Removing Punctuation and Special Characters:** Cleans the text to remove unnecessary symbols.
- **Removing Stopwords:** Filters out common words like *the*, *and*, *is* which do not add meaning.
- **Stemming:** Reduces words to their base form (e.g., *running* → *run*) to treat similar words the same.

### 3️⃣ Feature Extraction
The cleaned text is converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization**. This method measures the importance of each word relative to the entire dataset.

### 4️⃣ Model Training
A **Logistic Regression** classifier is trained on these numerical features to learn the patterns of spam and non-spam emails.

### 5️⃣ Model Saving
Once trained, the model and the TF-IDF vectorizer are saved using Pickle so they can be reused without retraining.

### 6️⃣ User Interface
A simple **Streamlit** web application is created so users can:
- Enter an email message.
- Click a button to classify the message.
- Instantly see if it’s **Spam** or **Ham**.

## 📦 Included Components

✅ Preprocessing with NLP techniques  
✅ TF-IDF Vectorization for feature extraction  
✅ Logistic Regression for classification  
✅ Streamlit app for real-time predictions  
✅ Pickled model and vectorizer for deployment

## 💡 Key Idea

By combining text processing and machine learning, the project turns raw email text into a structured format that a model can understand — allowing for accurate, real-time spam detection.

## 📌 Note

You can adapt this workflow to any similar text classification problem, such as sentiment analysis or fake news detection, by changing the dataset and retraining the model.


