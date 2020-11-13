import numpy as np
import math
import json
import os
import pdftotext
from bs4 import BeautifulSoup

from preprocess import process_sentence, preprocess
from get_15_word import get_first_15_words
from vectorize import vectorizer

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

def dot(vector_1, vector_2) :
    res = 0
    for i in range(len(vector_1)) :
        res += vector_1[i] * vector_2[i]
    return res
def norm (vector) :
    res = 0
    for i in range(len(vector)):
        res += vector[i] * vector[i]
    return math.sqrt(res)

def retrieve_information(query):

    all_links = load_links()

    all_titles = load_titles()

    all_first_15_words = load_first_15_words()

    # Load preprocess numpy array
    cleared_sentence_list = np.load("cleared_sentence.npy")

    # Process query
    query = [" ".join(process_sentence(query))]


    tfidf_documents,tfidf_query, list_kata = vectorizer(cleared_sentence_list, query)

    similarity = {}
    term = {}
    norm_query = norm(tfidf_query)
    for i in range(len(tfidf_documents)) :
        norm_document = norm(tfidf_documents[i])
        if norm_document * norm_query == 0:
            similarity[i] = 0
        else :
            similarity[i] = dot(tfidf_documents[i], tfidf_query) / (norm_document * norm_query)

    similarity_sorted = sorted(similarity.items(), key=lambda x: x[1], reverse=True)
    ranks = []
    term = {}
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
    for i in range(len(tfidf_query)) :
        if tfidf_query[i] != 0:
            term[list_kata[i]] = []
            for j in range(len(tfidf_documents)) :
                term[list_kata[i]].append(tfidf_documents[j][i])
    return ranks, term

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

    ranks, term = retrieve_information("gintama fullmetal alchemist")

    for i in range(len(ranks)):
        print(ranks[i])
    print(term)
