from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import json
import os
import pdftotext
from bs4 import BeautifulSoup

from preprocess import process_sentence, preprocess
from get_15_word import get_first_15_words
from vectorize import vectorize

baseURL = "http://127.0.0.1:5000/file/"

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
    # print(cleared_sentence_list)
    # print(cleared_sentence_list[0])
    # x = vectorize(cleared_sentence_list)
    # x = np.asarray(x)
    # print(x)
    # print("---")
    # x = np.transpose(x.T.toarray())
    # print(type(x))

    x, q_vec = vectorize(cleared_sentence_list, query)
    print(x)
    print(q_vec)
    # Vectorize query
    # q_vec = vectorize(query)
    # print(vectorizer.transform(query).toarray())
    # print("------------------------------------------------------")
    # print(query)
    # print(vectorizer.transform(query))
    # print(q_vec)

    similarity = {}

    # Get cosine similarity
    # for i in range(len(cleared_sentence_list)):
    #     if (np.linalg.norm(x[i]) * np.linalg.norm(q_vec)) == 0:
    #         similarity[i] = 0
    #     else:
    #         similarity[i] = np.dot(x[i], q_vec) / (np.linalg.norm(x[i]) * np.linalg.norm(q_vec))
    # Sort similarity
    similarity_sorted = sorted(similarity.items(), key=lambda x: x[1], reverse=True)
    ranks = []

    # Get ranks
    for indeks, sim in similarity_sorted:
        if sim != 0.0 :
            data = {
                "title" : all_titles[indeks],
                "links" : all_links[indeks],
                "first_15_words" : all_first_15_words[indeks],
                "similarity" : sim,
            }
            ranks.append(data)
    return ranks

def upload_file (file,filename) :
    if filename.lower().endswith(".pdf"):
        print(file)
        print("sampai sini")
        result = pdftotext.PDF(file)
        print(result)
        result = "\n\n".join(result)
        first_15_words = get_first_15_words(result)


        all_links = load_links()

        all_titles = load_titles()

        all_data = load_data()

        all_first_15_words = load_first_15_words()


        print(baseURL + filename)
        all_links.append(baseURL + filename)
        all_titles.append(filename)
        all_data.append(str(result))
        all_first_15_words.append(first_15_words)


        save_links(all_links)
        save_titles(all_titles)
        save_data(all_data)
        save_first_15_words(all_first_15_words)

        preprocess()
    elif filename.lower().endswith(".txt"):
        file_ = file.read()
        print(file_)
        first_15_words = get_first_15_words(str(file_))

        all_links = load_links()

        all_titles = load_titles()

        all_data = load_data()

        all_first_15_words = load_first_15_words()


        all_links.append(baseURL + filename)
        all_titles.append(filename)
        all_data.append(str(file_))
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

        all_links.append(baseURL + filename)
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

    print(retrieve_information("fullmetal tes"))
