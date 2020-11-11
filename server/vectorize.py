import numpy as np
import pandas as pd
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

def vectorize(arr, query):
    # print(arr)
    total_docs = len(arr)

    # To remove duplicate words from docs
    bag_words = []
    for i in range (total_docs):
        sentence = arr[i]
        words = sentence.split(" ")
        bag_words.append(words)
        if i == 0:
            unique_words = words
        else:
            unique_words = set(unique_words).union(set(words))

    # To remove duplicate words from query

    bag_query = []
    words_query = query.split()
    bag_query.append(words_query)
    unique_words = set(unique_words).union(set(words_query))


    # Search for occurence of every words from each documents and query
    words_list = list(unique_words)
    count_words = [[0 for j in range (len(words_list))] for i in range (total_docs+1)]
    for i in range (total_docs+1):
        if i != 0:
            bag_count = len(bag_words[i-1])
        else:
            bag_count = len(bag_query[i])
        for j in range (bag_count):
            if i != 0:
                bag = bag_words[i-1][j]
            else:
                bag = bag_query[i][j]
            if bag in words_list:
                idx = words_list.index(bag)
                count_words[i][idx] +=1

    # Compute TF
    tf = [[0 for j in range (len(words_list))] for i in range (total_docs+1)]
    for i in range (total_docs+1):
        if i != 0:
            bag_count = len(bag_words[i-1])
        else:
            bag_count = len(bag_query[i])
        for j in range (len(count_words[i])):
            tf[i][j] = count_words[i][j] / bag_count

    # Compute IDF
    idf = [0 for i in range (len(words_list))]
    for i in range (total_docs+1):
        for j in range (len(words_list)):
            if count_words[i][j] != 0:
                idf[j] += 1

    for j in range (len(words_list)):
        idf[j] = math.log(total_docs / idf[j])

    # Compute TF-IDF
    tfidf = [[0 for j in range (len(words_list))] for i in range (total_docs+1)]
    for i in range (total_docs+1):
        for j in range (len(words_list)):
            tfidf[i][j] = tf[i][j] * idf[j]
    quer = tfidf[0]
    words = np.delete(tfidf, 0, 0)
    print(quer)
    print(words)
    return words, quer

def newVectorize(arr,query) :
    data = {}
    banyakDokumen = len(arr)
    for i in range(len(arr)) :
        content = arr[i].split(" ")
        for kata in content :
            if kata not in data:
                data[kata] = [0] * (banyakDokumen + 1)
                data[kata][i] += 1
            else :
                data[kata][i] += 1
    query = query[0].split(" ")
    for kata in query :
        if kata not in data:
            data[kata] = [0] * (banyakDokumen + 1)
            data[kata][banyakDokumen] += 1
        else :
            data[kata][banyakDokumen] += 1
    documentVector = [[] for i in range(banyakDokumen)]
    queryVector = []
    for key in data.keys():
        for i in range(len(data[key])):
            if i < banyakDokumen :
                documentVector[i].append(data[key][i])
            else :
                queryVector.append(data[key][i])
    listKata = data.keys()
    # print(list(listKata))
    # print(documentVector)
    # print(queryVector)

    listKata = list(listKata)

    # Compute TF (ratio of every words)
    tf_document = [[0 for j in range (len(listKata))] for i in range (banyakDokumen)]
    tf_query = []
    # print(documentVector)
    for i in range (banyakDokumen+1):
        if i < banyakDokumen:
            total = sum(documentVector[i])
        else:
            total = sum(queryVector)
        for j in range (len(listKata)):
            if i < banyakDokumen:
                tf_document[i][j] = documentVector[i][j] / total
            else:
                tf_query.append(queryVector[j] / total)
    # print(tf_document)

    # Compute IDF
    idf = [0 for i in range (len(listKata))]
    idf_document = [0 for i in range (len(listKata))]
    idf_query = [0 for i in range (len(listKata))]
    for i in range (banyakDokumen):
        for j in range (len(listKata)):
            if documentVector[i][j] != 0:
                idf[j] += 1
    # print(idf)
    for i in range (len(listKata)):
        idf_document[i] = 1 + math.log(banyakDokumen / idf[i])
        if queryVector[i] != 0:
            idf_query[i] = idf_document[i]

    # Compute TF-IDF
    tfidf_documents = [[0 for j in range (len(listKata))] for i in range (banyakDokumen)]
    tfidf_query = [0 for i in range (len(listKata))]
    for i in range (banyakDokumen+1):
        for j in range (len(listKata)):
            if i < banyakDokumen:
                tfidf_documents[i][j] = tf_document[i][j] * idf_document[j]
            else:
                tfidf_query[j] = tf_query[j] * idf_query[j]

    # print(tfidf_documents)
    print()
    # print(tfidf_query)
    return (tfidf_documents,tfidf_query, list(listKata))

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

# if __name__ == "__main__" :
#     documentA = ['The game of life is a game of everlasting learning', 'The unexamined life is not worth living', 'Never stop learning']
#
#     tfidf_documents, tfidf_query, list_kata = newVectorize(documentA, ['The game of life is a game of everlasting'])
#
#     similarity = {}
#     term = {}
#     for i in range(len(tfidf_documents)) :
#         similarity[i] = dot(tfidf_documents[i], tfidf_query) / (norm(tfidf_documents[i]) * norm(tfidf_query))
#     for i in range(len(tfidf_query)) :
#         if tfidf_query[i] != 0:
#             term[list_kata[i]] = []
#             for j in range(len(tfidf_documents)) :
#                 term[list_kata[i]].append(tfidf_documents[j][i])
#     for keys in term.keys():
#         print(keys)
#         print(term[keys])
