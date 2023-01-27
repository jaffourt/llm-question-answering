import pickle
from typing import List

from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class LSASearchEngine:
    def __init__(self, docs: List[str], n_components=2):
        self.docs = docs
        self.n_components = n_components
        self.tfidf_vectorizer = TfidfVectorizer()
        self.lsa = TruncatedSVD(n_components=self.n_components)
        self.lsa_matrix = None

    def fit(self):
        tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.docs)
        self.lsa_matrix = self.lsa.fit_transform(tfidf_matrix)

    def search(self, query):
        # Generate the embeddings for the query
        query_embeddings = self.lsa.transform(self.tfidf_vectorizer.transform([query]))

        # Calculates the cosine similarity between query and docs
        similarities = cosine_similarity(query_embeddings, self.lsa_matrix)

        # Find the index of the most similar document
        most_similar_index = similarities.argmax()

        # return the most semantically similar document
        return self.docs[most_similar_index]

    def save(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, file_path):
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
        return model
