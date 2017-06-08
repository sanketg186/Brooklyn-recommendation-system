import pandas as pd
import numpy as np
from collections import OrderedDict

def collabrative(user_movies):
    movies_df = pd.read_csv('D:/pilot_project/brooklyn/movies/ml-latest-small/movies.csv')
    movies_df = pd.concat([movies_df, movies_df.genres.str.get_dummies(sep='|')], axis=1)
    movie_categories = movies_df.columns[3:]
    #print(movies_df.loc[0])
    #print(movies_df.head())
    user_preferences = OrderedDict(zip(movie_categories, []))

    ratings_df = pd.read_csv('D:/pilot_project/brooklyn/movies/ml-latest-small/ratings.csv')

    del ratings_df['timestamp']
    ratings_df = pd.merge(ratings_df, movies_df, on='movieId')[['userId', 'title', 'movieId', 'rating']]
    #print(ratings_df.head())
    ratings_mtx_df = ratings_df.pivot_table(values='rating', index='userId', columns='title')
    ratings_mtx_df.fillna(0, inplace=True)
    movie_index = ratings_mtx_df.columns
    #print(ratings_mtx_df.head())
    corr_matrix = np.corrcoef(ratings_mtx_df.T)
    #print(corr_matrix.shape)
    #favoured_movie_title = 'Toy Story (1995)'
    #favoured_movie_index = list(movie_index).index(favoured_movie_title)
    #P = corr_matrix[favoured_movie_index]
    #only return those movies with a high correlation with Toy Story
    #print(list(movie_index[(P>0.3) & (P<1.0)]))


    def get_movie_similarity(movie_title):
        #Returns correlation vector for a movie
        movie_idx = list(movie_index).index(movie_title)
        return corr_matrix[movie_idx]


    def get_movie_recommendations2(user_movies):
        #'''given a set of movies, it returns all the movies sorted by their correlation with the user'''
        movie_similarities = np.zeros(corr_matrix.shape[0])
        for movie_id in user_movies:
            movie_similarities = movie_similarities + get_movie_similarity(movie_id)
        similarities_df = pd.DataFrame({
            'movie_title': movie_index,
            'sum_similarity': movie_similarities
            })
        similarities_df = similarities_df[~(similarities_df.movie_title.isin(user_movies))]
        similarities_df = similarities_df.sort_values(by=['sum_similarity'], ascending=False)
        return similarities_df
    #sample_user = 21
    #print(ratings_df[ratings_df.userId==sample_user].sort_values(by=['rating'], ascending=False))

    #sample_user_movies = ratings_df[ratings_df.userId==sample_user].title.tolist()
    recommendations = get_movie_recommendations2(user_movies)

    #We get the top 20 recommended movies
    return recommendations.movie_title.head(20)