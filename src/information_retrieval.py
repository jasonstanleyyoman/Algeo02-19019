from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import json
import os
import pdftotext

from preprocess import process_sentence, preprocess


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

def save_links (all_links) :
    with open ("web-scrapping/links.json", "w") as file :
        json.dump(all_links,file)

def save_titles (all_data) :
    with open ("web-scrapping/titles.json", "w") as file :
        json.dump(all_data,file)

def save_data (all_titles) :
    with open ("web-scrapping/data.json", "w") as file :
        json.dump(all_titles,file)

def retrieve_information(query):

    all_links = load_links()

    all_titles = load_titles()

    # Load preprocess numpy array
    cleared_sentence_list = np.load("cleared_sentence.npy")

    # Process query
    query = [" ".join(process_sentence(query))]

    # Init vectorizer
    vectorizer = TfidfVectorizer()
    x = vectorizer.fit_transform(cleared_sentence_list)
    x = x.T.toarray()

    # Insert to data frame
    df = pd.DataFrame(x, index=vectorizer.get_feature_names())

    # Vectorize query
    q_vec = vectorizer.transform(query).toarray().reshape(df.shape[0],)
    similarity = {}

    # Get cosine similarity
    for i in range(len(cleared_sentence_list)):
        similarity[i] = np.dot(df.loc[:, i].values, q_vec) / np.linalg.norm(df.loc[:, i]) * np.linalg.norm(q_vec)
    # Sort similarity
    similarity_sorted = sorted(similarity.items(), key=lambda x: x[1], reverse=True)
    rank = []

    # Get ranks
    for k, v in similarity_sorted:
        if v != 0.0:
            data = {
                "title" : all_titles[k],
                "links" : all_links[k],
                "similarity" : v,
            }
            rank.append(data)
    return rank

def upload_file (file,filename) :
    if filename.lower().endswith(".pdf"):
        result = pdftotext.PDF(file)
        result = "\n\n".join(result)

        all_links = load_links()

        all_titles = load_titles()

        all_data = load_data()

        all_links.append(filename)
        all_titles.append(filename)
        all_data.append(str(result))

        save_links(all_links)
        save_titles(all_titles)
        save_data(all_data)

        preprocess()
    elif filename.lower().endswith(".txt"):
        file = file.read()
        all_links = load_links()

        all_titles = load_titles()

        all_data = load_data()

        all_links.append(filename)
        all_titles.append(filename)
        all_data.append(str(file))


        save_links(all_links)
        save_titles(all_titles)
        save_data(all_data)

        preprocess()
    #
    # preprocess()
# numpyarray = np.load("./cleared_sentence.npy")
# print(numpyarray)
