import math

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

    # Compute TF (ratio of every words)
    tf_document = [[0 for j in range (len(list_kata))] for i in range (banyak_dokumen)]
    tf_query = [0 for i in range (len(list_kata))]
    # print(document_vector)
    for i in range (banyak_dokumen+1):
        if i < banyak_dokumen:
            total = sum(document_vector[i])
        else:
            total = sum(query_vector)
        for j in range (len(list_kata)):
            if i < banyak_dokumen:
                tf_document[i][j] = document_vector[i][j] / total
            elif total != 0:
                tf_query[j] = query_vector[j] / total
    # End of Compute TF (ratio of every words)

    # Compute IDF
    idf = [0 for i in range (len(list_kata))]
    idf_document = [0 for i in range (len(list_kata))]
    idf_query = [0 for i in range (len(list_kata))]
    for i in range (banyak_dokumen):
        for j in range (len(list_kata)):
            if document_vector[i][j] != 0:
                idf[j] += 1

    for i in range (len(list_kata)):
        try:
            idf_document[i] = 1 + math.log(banyak_dokumen / idf[i])
        except e:
            print(e)
        if query_vector[i] != 0:
            idf_query[i] = idf_document[i]
    # End of Compute IDF

    # Compute TF-IDF
    tfidf_documents = [[0 for j in range (len(list_kata))] for i in range (banyak_dokumen)]
    tfidf_query = [0 for i in range (len(list_kata))]
    for i in range (banyak_dokumen+1):
        for j in range (len(list_kata)):
            if i < banyak_dokumen:
                tfidf_documents[i][j] = tf_document[i][j] * idf_document[j]
            else:
                tfidf_query[j] = tf_query[j] * idf_query[j]

    # End of Compute TF-IDF

    return (tfidf_documents,tfidf_query, list(list_kata))
# Compute Dot
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

if __name__ == "__main__" :
    documentA = ['The game of life is a game of everlasting learning', 'The unexamined life is not worth living', 'Never stop learning']
    query = ["unexamined"]
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
                term[query[i]].append(tfidf_documents[j][i])
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
