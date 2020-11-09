import numpy as np
import pandas as pd
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

def vectorize1(arr):
    length = len(arr)
    for i in range (length):
        sentence = arr[i]
        words = sentence.split()
        unique = set(words)
        arr_str = [0 for i in range (len(unique))]
        arr_count = [0 for i in range (len(unique))]
        before = 0
        for j in range (len(words)):
            if words[j] not in arr_str:
                arr_str[before] = words[j]
                arr_count[before] += 1
                before += 1
            else:
                where = arr_str.index(words[j])
                arr_count[where] += 1
        print(arr_count)
        new_arr_count = decimalize(arr_count, len(words))
        if i == 0:
            overall = [[]]
            overall[0] = new_arr_count
        # else:
        #     print(overall)
        #     arr_count = [arr_count]
        #     np.concatenate((overall, arr_count), axis = 0)
        print("-------")
        print(overall, i)
        arr_str.clear()
        arr_count.clear()

arr = ['ya hem iya ya hem meong', 'lalalala kamu siapa sih']
# vectorize(arr)

def vectorize2(arr):
    # print(arr)
    total_docs = len(arr)
    

    # To remove duplicate words
    bag_words = []
    for i in range (total_docs):
        sentence = arr[i]
        words = sentence.split()
        bag_words.append(words)
        if i == 0:
            unique_words = words
        else:
            unique_words = set(unique_words).union(set(words))
    
    # print(bag_words)
    # print(unique_words)

    # Search for occurence every words from each documents
    words_list = list(unique_words)
    count_words = [[0 for j in range (len(words_list))] for i in range (total_docs)]
    
    for i in range (total_docs):
        for j in range (len(words_list)):
            if j < len(bag_words[i]):
                if bag_words[i][j] in words_list:
                    idx = words_list.index(bag_words[i][j])
                    count_words[i][idx] += 1
    # print(count_words)
    
    # Compute TF
    tf = [[0 for j in range (len(words_list))] for i in range (total_docs)]
    for i in range (total_docs):
        bag_words_count = len(bag_words[i])
        for j in range (len(count_words[i])):
            tf[i][j] = count_words[i][j] / bag_words_count

    # print(tf)
    print(total_docs)
    # Compute IDF
    idf = [0 for i in range (len(words_list))]
    for i in range (total_docs):
        for j in range (len(words_list)):
            if count_words[i][j] != 0:
                idf[j] += 1

    for j in range (len(words_list)):
        print(idf[j])
        idf[j] = math.log(total_docs / idf[j])

    # print(idf)
    # Compute TF-IDF
    tfidf = [[0 for j in range (len(words_list))] for i in range (total_docs)]
    for i in range (total_docs):
        for j in range (len(words_list)):
            tfidf[i][j] = tf[i][j] * idf[j]
    # x = np.transpose(tfidf.toarray())
    print(tfidf)
    return tfidf

def doc_freq(word):
    c = 0
    try:
        c = DF[word]
    except:
        pass
    return c

def vectorize(arr):
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

vectorize2(documentA)