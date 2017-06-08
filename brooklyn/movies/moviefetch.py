import pandas as pd
from .poster import imdb_id_from_title
from .poster import getposter
def get_all_movies():
    movies_df = pd.read_csv('D:/pilot_project/brooklyn/movies/ml-latest-small/movies.csv')
    movies_df = pd.concat([movies_df, movies_df.genres.str.get_dummies(sep='|')], axis=1)
    all_movies = []
    all_movies = movies_df['title']
    return all_movies


def getmovieid(movielist):
    movieid_list = []
    for title in movielist:
        movieid_list.append(imdb_id_from_title(title))
    return movieid_list


def getmovieposter(movieid_list):
    movie_url_list = []
    for id in movieid_list:
        movie_url_list.append(getposter(id))
    return movie_url_list