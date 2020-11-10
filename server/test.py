from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

documentA = ['The game of life is a game of everlasting learning', 'The unexamined life is not worth living', 'Never stop learning']
query = "game game living"
query = [query]

vectorizer = TfidfVectorizer()
# print(vectorizer.fit_transform(documentA))
x = vectorizer.fit_transform(documentA)
print(np.transpose(x.T.toarray()))
# print(vectorizer.transform(query))
print("------")
print(vectorizer.transform(query).toarray()[0])