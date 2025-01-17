#from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import json
import os
import pdftotext
from bs4 import BeautifulSoup
import math

from preprocess import process_sentence, preprocess
from get_15_word import get_first_15_words
from total_words import get_total_words
from vectorize import vectorizer

baseURL = "http://127.0.0.1:5000/file/"

# Calculate dot product of 2 vector
def dot(vector_1, vector_2) :
    res = 0
    for i in range(len(vector_1)) :
        res += vector_1[i] * vector_2[i]
    return res
# Calculate norm of vector
def norm (vector) :
    res = 0
    for i in range(len(vector)):
        res += vector[i] * vector[i]
    return math.sqrt(res)

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

def load_total_words () :
    with open ("web-scrapping/total_words.json") as file :
        all_total_words = json.load(file)
        return all_total_words

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

def save_total_words (all_total_words) :
    with open ("web-scrapping/total_words.json", "w") as file :
        json.dump(all_total_words,file)


def retrieve_information(query):
    # Load all data
    all_links           = load_links()
    all_titles          = load_titles()
    all_first_15_words  = load_first_15_words()
    all_total_words     = load_total_words()

    # Load preprocess numpy array
    cleared_sentence_list = np.load("cleared_sentence.npy")

    # Process query
    query = [" ".join(process_sentence(query))]

    # Vectorize query and document
    tfidf_documents,tfidf_query, list_kata = vectorizer(cleared_sentence_list, query)

    similarity = {}
    term = {}
    norm_query = norm(tfidf_query)
    # Calculate similarity
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
                "total_words" : all_total_words[indeks],
                "similarity" : sim,
            }
            ranks.append(data)
    query = query[0].split(" ")

    # Calculate term
    for i in range(len(query)) :
        if query[i] in list_kata:
            indeks = list_kata.index(query[i])
            term[query[i]] = []
            for j in range(len(tfidf_documents)) :
                term[query[i]].append(tfidf_documents[j][indeks])
        else :
            term[query[i]] = [0] * len(tfidf_documents)
    return ranks, term, all_titles
def upload_file (file,filename, original_filename) :
    if filename.lower().endswith(".pdf"):
        result          = pdftotext.PDF(file)
        result          = "\n\n".join(result)
        first_15_words  = get_first_15_words(result)
        total_words     = get_total_words(result)

        # Load all data
        all_links           = load_links()
        all_titles          = load_titles()
        all_data            = load_data()
        all_first_15_words  = load_first_15_words()
        all_total_words     = load_total_words()


        all_links.append(baseURL + filename)
        all_titles.append(original_filename)
        all_data.append(str(result))
        all_first_15_words.append(first_15_words)
        all_total_words.append(total_words)


        save_links(all_links)
        save_titles(all_titles)
        save_data(all_data)
        save_first_15_words(all_first_15_words)
        save_total_words(all_total_words)

        preprocess()
    elif filename.lower().endswith(".txt"):
        file_           = file.read()
        first_15_words  = get_first_15_words(str(file_))
        total_words     = get_total_words(str(file_))

        # Load all data
        all_links           = load_links()
        all_titles          = load_titles()
        all_data            = load_data()
        all_first_15_words  = load_first_15_words()
        all_total_words     = load_total_words()

        all_links.append(baseURL + filename)
        all_titles.append(original_filename)
        all_data.append(str(file_))
        all_first_15_words.append(first_15_words)
        all_total_words.append(total_words)

        save_links(all_links)
        save_titles(all_titles)
        save_data(all_data)
        save_first_15_words(all_first_15_words)
        save_total_words(all_total_words)

        preprocess()
    elif filename.lower().endswith(".html"):
        soup            = BeautifulSoup(file,"html.parser")
        text            = soup.text
        first_15_words  = get_first_15_words(text)
        total_words     = get_total_words(text)

        # Load all data
        all_links           = load_links()
        all_titles          = load_titles()
        all_data            = load_data()
        all_first_15_words  = load_first_15_words()
        all_total_words     = load_total_words()

        all_links.append(baseURL + filename)
        all_titles.append(original_filename)
        all_data.append(str(text))
        all_first_15_words.append(first_15_words)
        all_total_words.append(total_words)

        save_links(all_links)
        save_titles(all_titles)
        save_data(all_data)
        save_first_15_words(all_first_15_words)
        save_total_words(all_total_words)

        preprocess()
