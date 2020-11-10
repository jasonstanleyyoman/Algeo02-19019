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
        words = sentence.split()
        bag_words.append(words)
        if i == 0:
            unique_words = words
        else:
            unique_words = set(unique_words).union(set(words))
    
    # To remove duplicate words from query
    bag_query = []
    words_query = query[0].split()
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

def doc_freq(word):
    c = 0
    try:
        c = DF[word]
    except:
        pass
    return c

def vectorize1(arr):
    total_docs = len(arr)

    # Convert list to dict
    words_dict = {}
    for i in range (total_docs):
        sentence = arr[i]
        words = sentence.split()
        for x in words:
            try :
                words_dict[x].add(i)
            except:
                words_dict[x] = {i}

    # Calculate occurence of every words
    for i in words_dict:
        words_dict[i] = len(words_dict[i])

    # Compute TF-IDF
    doc = 0
    tf_idf= {}
    N = total_docs
    for i in range(N):    
        tokens = arr[i]
        counter = Counter(tokens)
        words_count = len(tokens)
        for token in np.unique(tokens): 
            tf = counter[token]/words_count
            df = doc_freq(token)
            idf = np.log((N+1)/(df+1)) 
            tf_idf[doc, token] = tf*idf
        doc += 1
    print(tf_idf)
    
documentA = ['the man went out for a walk walk', 'the children sat around the fire']

vectorize(documentA, 'hello')