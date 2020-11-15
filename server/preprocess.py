from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
import nltk
import pandas as pd
import numpy as np
import json

# Tokenizer sekalian menghapus punctuation
tokenizer = RegexpTokenizer(r'\w+')

# List stop words
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Porter Stemmer untuk stemming
porter = PorterStemmer()

# Menghapus stopwords dan melakukan stemming sebuah kalimat
def process_sentence(sentence):

    sentence = tokenizer.tokenize(sentence)

    # Menghapus stop words
    stop_words_removed = [word for word in sentence if word not in stop_words]

    # Stemming
    stemmed_words = [porter.stem(word) for word in stop_words_removed]

    return stemmed_words

def preprocess() :
    with open ("web-scrapping/data.json") as file:
        all_sentence_list = json.load(file)

        # Memproses setiap kalimat
        cleared_sentence_list = [" ".join(process_sentence(sentence)) for sentence in all_sentence_list]

        np.save("cleared_sentence",cleared_sentence_list)
