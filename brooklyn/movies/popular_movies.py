import tmdbsimple as ts
ts.API_KEY = '72d232fb4cb9aa3fa5049aec63a1ebf9'
movies = ts.Movies()
x=[]
x=movies.popular()
movie_title = []
movie_poster = []
movie_overview = []


def pop_mov():

    for y in x['results']:
        movie_title.append(y['title'])
        movie_poster.append('http://image.tmdb.org/t/p/w185'+y['poster_path'])
        movie_overview.append(y['overview'])
    return movie_title, movie_overview, movie_poster