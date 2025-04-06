# recommender.py
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from surprise import SVD, Dataset, Reader

class HybridRecommender:
    def __init__(self, movies_path, ratings_path, genres_encoded_path):
        self.movies = pd.read_csv(movies_path)
        self.ratings = pd.read_csv(ratings_path)
        self.genres_encoded = pd.read_csv(genres_encoded_path, index_col=0)

        self.similarity_matrix = cosine_similarity(self.genres_encoded.values)
        self.movieId_to_index = {mid: idx for idx, mid in enumerate(self.genres_encoded.index)}
        self.index_to_movieId = {idx: mid for mid, idx in self.movieId_to_index.items()}

        self._train_cf_model()

    def _train_cf_model(self):
        reader = Reader(rating_scale=(0.5, 5.0))
        data = Dataset.load_from_df(self.ratings[['userId', 'movieId', 'rating']], reader)
        trainset = data.build_full_trainset()
        self.cf_model = SVD()
        self.cf_model.fit(trainset)

    def get_users(self):
        return self.ratings['userId'].unique()

    def get_user_high_rated_movies(self, user_id, threshold=4.0):
        return self.ratings[(self.ratings['userId'] == user_id) & (self.ratings['rating'] >= threshold)]

    def get_movie_title(self, movie_id):
        title = self.movies[self.movies['movieId'] == movie_id]['title'].values
        return title[0] if len(title) > 0 else None

    def recommend(self, user_id, top_n=5):
        user_ratings = self.get_user_high_rated_movies(user_id)
        liked_movie_ids = user_ratings['movieId'].tolist()
        liked_indices = [self.movieId_to_index[mid] for mid in liked_movie_ids if mid in self.movieId_to_index]

        if not liked_indices:
            return []

        mean_sim = np.mean(self.similarity_matrix[liked_indices], axis=0)
        hybrid_scores = {}

        for idx in range(len(mean_sim)):
            movie_id = self.index_to_movieId[idx]
            if movie_id in liked_movie_ids:
                continue

            content_score = mean_sim[idx]
            try:
                collab_score = self.cf_model.predict(user_id, movie_id).est
            except:
                collab_score = 0

            hybrid_score = 0.5 * content_score + 0.5 * (collab_score / 5.0)
            hybrid_scores[movie_id] = hybrid_score

        sorted_movies = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)
        recommendations = []
        for movie_id, _ in sorted_movies[:top_n]:
            title = self.get_movie_title(movie_id)
            if title:
                recommendations.append(title)

        return recommendations