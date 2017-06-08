import requests


def imdb_id_from_title(title):
    title = title[0:len(title)-6]
    pattern = "http://www.imdb.com/xml/find?json=1&nr=1&tt=on&q="+title
    print(pattern)
    # url = pattern.format(movie_title=urllib.request(title))
    r = requests.get(pattern)
    res = r.json()
    # sections in descending order or preference
    for section in ['popular', 'exact', 'substring']:
        key = 'title_' + section
        if key in res:
            return res[key][0]['id']


def getposter(movieid):
    CONFIG_PATTERN = "https://api.themoviedb.org/3/movie/"+str(movieid)+"?api_key=72d232fb4cb9aa3fa5049aec63a1ebf9"
    print(CONFIG_PATTERN)
    KEY = '72d232fb4cb9aa3fa5049aec63a1ebf9'
    url = CONFIG_PATTERN.format(key=KEY)
    check = requests.head(url)
    x=check.status_code == requests.codes.ok
    if x is False:
        return "http://www.freeiconspng.com/uploads/no-image-icon-15.png"
    else:
        r = requests.get(url)
        config = r.json()
        print(config['poster_path'])
        base_url = 'http://image.tmdb.org/t/p/w185'
        complete_url = base_url+config['poster_path']
        return complete_url