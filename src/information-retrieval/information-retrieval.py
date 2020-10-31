from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import json

from preprocess import process_sentence

def retrieve_information(query):
    with open ("../web-scrapping/links.json") as file :
        all_links = json.load(file)
    with open ("../web-scrapping/titles.json") as file :
        all_titles = json.load(file)
    # Load preprocess numpy array
    cleared_sentence_list = np.load("cleared_sentence_list.npy")

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
    similarity_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)
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

ranks = retrieve_information("gintama")
for rank in ranks:
    print(rank)
