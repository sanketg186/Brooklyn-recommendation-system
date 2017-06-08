import pandas as pd
import numpy as np
from collections import OrderedDict
from .models import GenreSelect


def contentbased(genre):

    def dot_product(vector_1, vector_2):
        return sum([i*j for i, j in zip(vector_1, vector_2)])

    def get_movie_score(movie_features, user_preferences):
        return dot_product(movie_features, user_preferences)

    def get_movie_recommendations(user_preferences, n_recommendations):
        movies_df['score'] = movies_df[movie_categories].apply(get_movie_score,
                                                               args=([user_preferences.values()]), axis=1)
        return movies_df.sort_values(by=['score'], ascending=False)['title'][:n_recommendations]

    movies_df = pd.read_csv('D:/pilot_project/brooklyn/movies/ml-latest-small/movies.csv')
    movies_df = pd.concat([movies_df, movies_df.genres.str.get_dummies(sep='|')], axis=1)
    movie_categories = movies_df.columns[3:]
    user_preferences = OrderedDict(zip(movie_categories, []))

    genre = list(map(int, genre))
    user_preferences['(no genres listed) '] = 0
    user_preferences['Action'] = genre[0]
    user_preferences['Adventure'] = genre[1]
    user_preferences['Animation'] = genre[2]
    user_preferences["Children's"] = genre[3]
    user_preferences["Comedy"] = genre[4]
    user_preferences['Crime'] = genre[5]
    user_preferences['Documentary'] = genre[6]
    user_preferences['Drama'] = genre[7]
    user_preferences['Fantasy'] = genre[8]
    user_preferences['Film-Noir'] = genre[9]
    user_preferences['Horror'] = genre[10]
    user_preferences['IMAX'] = 0
    user_preferences['Musical'] = genre[11]
    user_preferences['Mystery'] = genre[12]
    user_preferences['Romance'] = genre[13]
    user_preferences['Sci-Fi'] = genre[14]
    user_preferences['War'] = genre[15]
    user_preferences['Thriller'] = genre[16]
    user_preferences['Western'] = genre[17]
    return get_movie_recommendations(user_preferences, 5)