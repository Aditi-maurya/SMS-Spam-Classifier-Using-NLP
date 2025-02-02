import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
nltk.data.path.append(r'C:\nltk_data')

nltk.download('punkt', download_dir=r'C:\nltk_data')
nltk.download('stopwords', download_dir=r'C:\nltk_data')
nltk.download('punkt_tab', download_dir=r'C:\nltk_data')

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
import nltk
nltk.download('punkt')
nltk.download('stopwords')

import nltk

# Specify a custom directory for nltk data
nltk.data.path.append(r'C:\nltk_data')

# Download the punkt tokenizer to this directory
nltk.download('punkt', download_dir=r'C:\nltk_data')
import nltk
print(nltk.data.find('tokenizers/punkt'))

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

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")
input_sms = st.text_input("Enter the message")
if st.button('Predict'):

    # preprocess
    transformed_sms = transform_text(input_sms)
    # vectorize
    vector_input = tfidf.transform([transformed_sms ])
    # predict
    result = model.predict(vector_input)[0]
    # display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

