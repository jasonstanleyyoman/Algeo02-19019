from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import json
import os
import pdftotext
from bs4 import BeautifulSoup

from .preprocess import process_sentence, preprocess
from .get_15_word import get_first_15_words


def load_links () :
    with open ("web-scrapping/links.json") as file :
        all_links = json.load(file)
        return all_links
def load_titles () :
    with open ("web-scrapping/titles.json") as file :
        all_titles = json.load(file)
        return all_titles

def load_data () :
    with open ("web-scrapping/data.json") as file :
        all_data = json.load(file)
        return all_data

def load_first_15_words () :
    with open ("web-scrapping/first_15_word.json") as file :
        all_first_15_words = json.load(file)
        return all_first_15_words

def save_links (all_links) :
    with open ("web-scrapping/links.json", "w") as file :
        json.dump(all_links,file)

def save_titles (all_data) :
    with open ("web-scrapping/titles.json", "w") as file :
        json.dump(all_data,file)

def save_data (all_titles) :
    with open ("web-scrapping/data.json", "w") as file :
        json.dump(all_titles,file)

def save_first_15_words (all_first_15_words) :
    with open ("web-scrapping/first_15_word.json", "w") as file :
        json.dump(all_first_15_words,file)
def retrieve_information(query):

    all_links = load_links()

    all_titles = load_titles()

    all_first_15_words = load_first_15_words()

    # Load preprocess numpy array
    cleared_sentence_list = np.load("cleared_sentence.npy")
    # Process query
    query = [" ".join(process_sentence(query))]

    # Init vectorizer
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(cleared_sentence_list)
    x = np.transpose(x.T.toarray())

    # Vectorize query
    q_vec = vectorizer.transform(query).toarray()[0]

    similarity = {}

    # Get cosine similarity
    for i in range(len(cleared_sentence_list)):
        similarity[i] = np.dot(x[i], q_vec) / (np.linalg.norm(x[i]) * np.linalg.norm(q_vec))
    # Sort similarity
    similarity_sorted = sorted(similarity.items(), key=lambda x: x[1], reverse=True)
    ranks = []

    # Get ranks
    for indeks, sim in similarity_sorted:
        if sim != 0.0:
            data = {
                "title" : all_titles[indeks],
                "links" : all_links[indeks],
                "first_15_words" : all_first_15_words[indeks]
                "similarity" : sim,
            }
            ranks.append(data)
    return ranks

def upload_file (file,filename) :
    if filename.lower().endswith(".pdf"):
        result = pdftotext.PDF(file)
        result = "\n\n".join(result)
        first_15_words = get_first_15_words(result)


        all_links = load_links()

        all_titles = load_titles()

        all_data = load_data()

        all_first_15_words = load_first_15_words()



        all_links.append(filename)
        all_titles.append(filename)
        all_data.append(str(result))
        all_first_15_words.append(first_15_words)


        save_links(all_links)
        save_titles(all_titles)
        save_data(all_data)
        save_first_15_words(all_first_15_words)

        preprocess()
    elif filename.lower().endswith(".txt"):
        file = file.read()
        first_15_words = get_first_15_words(str(file))

        all_links = load_links()

        all_titles = load_titles()

        all_data = load_data()

        all_first_15_words = load_first_15_words()

        all_links.append(filename)
        all_titles.append(filename)
        all_data.append(str(file))
        all_first_15_words.append(first_15_words)


        save_links(all_links)
        save_titles(all_titles)
        save_data(all_data)
        save_first_15_words(all_first_15_words)

        preprocess()
    elif filename.lower().endswith(".doc"):
        pass
    elif filename.lower().endswith(".html"):
        soup = BeautifulSoup(file,"html.parser")
        text = soup.text
        first_15_words = get_first_15_words(file)

        all_links = load_links()

        all_titles = load_titles()

        all_data = load_data()

        all_first_15_words = load_first_15_words()

        all_links.append(filename)
        all_titles.append(filename)
        all_data.append(str(text))
        all_first_15_words.append(first_15_words)

        save_links(all_links)
        save_titles(all_titles)
        save_data(all_data)
        save_first_15_words(all_first_15_words)

        preprocess()

    #

    # preprocess()

if __name__ == "__main__" :

    print(retrieve_information("metal")[0]["title"])
