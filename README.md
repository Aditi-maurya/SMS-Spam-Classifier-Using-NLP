# 📩 SMS Spam Classifier

An SMS spam classifier is a machine learning-based system that automatically categorizes incoming SMS messages as either spam or ham (not spam).In the era of digital communication, SMS (Short Message Service) has become a widely used mode of communication. However, with its popularity, the issue of spam messages has increased significantly. These spam messages include promotional offers, phishing attempts, and fraudulent schemes. To combat this, an SMS Spam Classifier using Natural Language Processing (NLP) is developed to automatically detect and filter spam messages from genuine ones (ham messages).The goal of an SMS spam classifier is to identify and filter out spam messages, ensuring a better user experience.

---

## 🔍 Project Overview

This project walks through a complete ML pipeline:
- Data cleaning
- Exploratory Data Analysis (EDA)
- Text preprocessing using NLP
- Feature extraction via vectorization
- Model training & evaluation
- Ready for deployment as a web service

---

## 🧠 Features

- 📥 **Dataset Ingestion** – Reads labeled SMS data from a CSV file
- 🧹 **Text Preprocessing** – Tokenization, stopword & punctuation removal, stemming
- 📊 **EDA** – 
  - Class distribution visualization (spam vs ham)
  - Message length, word count & sentence count analysis
- 🏗️ **Feature Engineering** – Numerical features like `num_characters`, `num_words`, and `num_sentences`
- 🧠 **Model Training** – 
  - Naive Bayes classifier using CountVectorizer and TF-IDF
- 📈 **Model Evaluation** – 
  - Accuracy, precision, recall, confusion matrix
- 💡 **Imbalanced Data Handling** – Visual feedback on class imbalance

---

## ⚙️ Tech Stack

| Layer           | Tools & Libraries                           |
|-----------------|----------------------------------------------|
| Language        | Python                                       |
| Data Handling   | `pandas`, `numpy`                            |
| Visualization   | `matplotlib`, `seaborn`                      |
| NLP             | `nltk`, `string`, `re`                       |
| ML Model        | `sklearn` (Naive Bayes, CountVectorizer, etc.) |
| Notebook Env    | Jupyter Notebook                             |

---

## 🔄 How It Works

1. **Load & Clean Data**
   - Drops irrelevant columns
   - Renames `v1` to `target`, `v2` to `text`
   - Encodes spam/ham into 1/0
   - Removes duplicates

2. **EDA**
   - Pie charts of spam/ham ratio
   - Histograms of message lengths
   - Heatmaps for correlation

3. **Text Preprocessing**
   - Lowercasing
   - Tokenization using `nltk`
   - Removing stopwords and punctuation
   - Stemming using `PorterStemmer`

4. **Vectorization**
   - Transforms clean text into numerical features using:
     - `CountVectorizer`
     - `TfidfVectorizer`

5. **Model Training & Evaluation**
   - Naive Bayes classifier trained on the features
   - Performance analyzed using confusion matrix and classification report

---

## 📁 Project Structure

