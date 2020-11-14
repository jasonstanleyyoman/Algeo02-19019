import math

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

# Compute TF
def ratio(vector, total, dict_length, tf):
    for i in range (dict_length):
        tf[i] = vector[i] / total
    return tf

def TF(document, query, dict_length, total_docs):
    tf_document = [[0 for j in range (dict_length)] for i in range (total_docs)]
    tf_query = [0 for i in range (dict_length)]
    for i in range (total_docs+1):
        if i < total_docs:
            total = sum(document[i])
            tf_document[i] = ratio(document[i], total, dict_length, tf_document[i])
        else:
            total = sum(query)
            if total != 0:
                tf_query = ratio(query, total, dict_length, tf_query)
    return tf_document, tf_query
# End of Compute TF

# Compute IDF
def IDF(dict_length, total_docs, document, query):
    idf = [0 for i in range (dict_length)]
    idf_doc = idf
    idf_que = idf
    for i in range (total_docs):
        for j in range (dict_length):
            if document[i][j] != 0:
                idf[j] +=1

    for i in range (dict_length):
        idf_doc[i] = math.log(total_docs / idf[i])
        if query[i] != 0:
            idf_que[i] = idf_doc[i]
    return idf_doc, idf_que
# End of Compute IDF

# Compute TF-IDF
def TF_IDF(dict_length, total_docs, document, query):
    tfidf_doc = [[0 for j in range (dict_length)] for i in range (total_docs)]
    tfidf_que = [0 for i in range (dict_length)]

    tf_doc, tf_que = TF(document, query, dict_length, total_docs)
    idf_doc, idf_que = IDF(dict_length, total_docs, document, query)

    for i in range (total_docs+1):
        for j in range (dict_length):
            if i < total_docs:
                tfidf_doc[i][j] = tf_doc[i][j] * idf_doc[j]
            else:
                tfidf_que[j] = tf_que[j] * idf_que[j]
    return tfidf_doc, tfidf_que
# End of Compute TF-IDF

# Compute TFIDF of document and query
def vectorizer(arr,query) :
    # Listing of unique word
    data = {}
    banyak_dokumen = len(arr)
    for i in range(len(arr)) :
        content = arr[i].split(" ")
        for kata in content :
            if kata not in data:
                data[kata] = [0] * (banyak_dokumen)
                data[kata][i] += 1
            else :
                data[kata][i] += 1
    document_vector = [[] for i in range(banyak_dokumen)]

    for key in data.keys():
        for i in range(len(data[key])):
            document_vector[i].append(data[key][i])

    list_kata = list(data.keys())
    query_vector = [0] * len(list_kata)
    query_arr = query[0].split(" ")
    for i in range(len(query_arr)):
        content = query_arr[i]
        if content in list_kata :
            query_vector[list_kata.index(content)] += 1
    # End of Listing of unique word

    list_kata = list(list_kata)

    # Compute TF-IDF
    tfidf_documents, tfidf_query = TF_IDF(len(list_kata), banyak_dokumen, document_vector, query_vector)

    return (tfidf_documents,tfidf_query, list(list_kata))

if __name__ == "__main__" :
    documentA = ['The game of life is a game of everlasting learning', 'The unexamined life is not worth living', 'Never stop learning']
    query = ["learning"]
    tfidf_documents, tfidf_query, list_kata = vectorizer(documentA, query)
    print(tfidf_documents)
    print("---")
    print(tfidf_query)
    print("---")
    print(list_kata)


    similarity = {}
    term = {}
    norm_query = norm(tfidf_query)
    for i in range(len(tfidf_documents)) :
        norm_document = norm(tfidf_documents[i])
        if norm_document * norm_query == 0:
            similarity[i] = 0
        else :
            similarity[i] = dot(tfidf_documents[i], tfidf_query) / (norm_document * norm_query)
    query = query[0].split(" ")
    for i in range(len(query)) :
        if query[i] in list_kata:
            indeks = list_kata.index(query[i])
            term[query[i]] = []
            for j in range(len(tfidf_documents)) :
                term[query[i]].append(tfidf_documents[j][indeks])
        else :
            term[query[i]] = [0] * len(tfidf_documents)


    # for i in range(len(tfidf_query)) :
    #     if tfidf_query[i] != 0:
    #         term[list_kata[i]] = []
    #         for j in range(len(tfidf_documents)) :
    #             term[list_kata[i]].append(tfidf_documents[j][i])


    print(similarity)
    similarity_sorted = sorted(similarity.items(), key=lambda x: x[1], reverse=True)
    print(similarity_sorted)
    print(term)
