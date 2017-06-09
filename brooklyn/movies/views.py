from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import View
from .forms import UserForm
from .models import GenreSelect, UserRating,Movies
from .rateform import RateForm
from .contentbased import contentbased
from .collabrative import collabrative
from .poster import imdb_id_from_title
from .poster import getposter
from .moviefetch import get_all_movies, getmovieid, getmovieposter
from .search import get_query
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import operator
from .popular_movies import pop_mov
# Create your views here.


genrelist = {'genreaction': 'Action', 'genreadventure': 'Adventure',
             'genreanimation': 'Animation', 'genrechildren': 'Children',
             'genrecomedy': 'Comedy', 'genrecrime': 'Crime',
             'genredocumentary': 'Documentary', 'genredrama': 'Drama',
             'genrefantasy': 'Fantasy', 'genrefilmnoir': 'Filmnoir',
             'genrehorror': 'Horror', 'genremusical': 'Musical', 'genremystery': 'Mystery',
             'genreromance': 'Romance', 'genrescifi': 'Scifi', 'genrethriller': 'Thriller',
             'genrewar': 'War', 'genrewestern': 'Western'}


def index(request):
    template_name = 'movies/index.html'
    movie_title,movie_overview,movie_poster = pop_mov()
    movie_detail = zip(movie_title, movie_overview, movie_poster)
    return render(request, template_name, {'genrelist': genrelist, 'movie_detail': movie_detail})


def pref(request):
    x = []
    prefe = get_object_or_404(GenreSelect)
    prefe.Action = request.POST.get('genreaction')
    x.append(prefe.Action)
    prefe.Adventure = request.POST.get('genreadventure')
    x.append(prefe.Adventure)
    prefe.Animation = request.POST.get('genreanimation')
    x.append(prefe.Animation)
    prefe.Children = request.POST.get('genrechildren')
    x.append(prefe.Children)
    prefe.Comedy = request.POST.get('genrecomedy')
    x.append(prefe.Comedy)
    prefe.Crime = request.POST.get('genrecrime')
    x.append(prefe.Crime)
    prefe.Documentary = request.POST.get('genredocumentary')
    x.append(prefe.Documentary)
    prefe.Drama = request.POST.get('genredrama')
    x.append(prefe.Drama)
    prefe.Fantasy = request.POST.get('genrefantasy')
    x.append(prefe.Fantasy)
    prefe.FilmNoir = request.POST.get('genrefilmnoir')
    x.append(prefe.FilmNoir)
    prefe.Horror = request.POST.get('genrehorror')
    x.append(prefe.Horror)
    prefe.Musical = request.POST.get('genremusical')
    x.append(prefe.Musical)
    prefe.Mystery = request.POST.get('genremystery')
    x.append(prefe.Mystery)
    prefe.Romance = request.POST.get('genreromance')
    x.append(prefe.Romance)
    prefe.SciFi = request.POST.get('genrescifi')
    x.append(prefe.SciFi)
    prefe.Thriller = request.POST.get('genrethriller')
    x.append(prefe.Thriller)
    prefe.War = request.POST.get('genrewar')
    x.append(prefe.War)
    prefe.Western = request.POST.get('genrewestern')
    x.append(prefe.Western)
    prefe.save()
    moviename=[]
    movieid=[]
    movieurl=[]
    y = contentbased(x)
    for j in y:
        moviename.append(j)
        movieid.append(imdb_id_from_title(j))
    #print(movieid)
    for i in movieid:
        if i is not None:
            movieurl.append(getposter(i))
        else:
            movieurl.append("D:/pilot_project/brooklyn/movies/static/movies/images/noimage.png")
    movienameurl = dict(zip(moviename, movieurl))




    return render(request, 'movies/contentbased.html', {'pref': prefe, 'genrelist': genrelist, 'movienameurl':movienameurl})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'movies/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Album.objects.filter(user=request.user)
                return render(request, 'movies/index.html')
            else:
                return render(request, 'movies/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'movies/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'movies/index.html')
    context = {
        "form": form,
    }
    return render(request, 'movies/register.html', context)


def rate(request):
    if request.method == 'POST':
        user = request.user
        movie_title = request.POST.get('movie_name')
        rating = request.POST.get('movie_rate')
        rateobj = UserRating(user = user, movie_title = movie_title, rating = rating)
        rateobj.save()
    movie_list = []
    movie_list = get_all_movies()
    paginator = Paginator(movie_list, 3)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)
    movieid = getmovieid(movies)
    moviurl = getmovieposter(movieid)
    movienameurl = dict(zip(movies, moviurl))

    return render(request, 'movies/rate.html', {'movienameurl': movienameurl, 'movies': movies})


def similar_movie(request):
    user_movies = []
    movie_name = []
    movie_rating = []
    user_movies = list(UserRating.objects.filter(user=request.user))
    print(user_movies)
    for i in user_movies:
        x = str(i)
        movie_rating.append(int(x[0]))
        movie_name.append(x[1::])
    #print(movie_name[0])
    #print(movie_rating[0])
    user_movie_rate = dict(zip(movie_name, movie_rating))
    user_movies = sorted(user_movie_rate.items(), key=operator.itemgetter(1), reverse=True)
    movie_name = []
    for k, v in user_movies:
        movie_name.append(k)
        print(movie_name)
    recommend_movies = []
    recommend_movies = collabrative(movie_name)
    #print(recommend_movies)


    paginator = Paginator(recommend_movies, 3)
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)
    movieid = getmovieid(movies)
    moviurl = getmovieposter(movieid)
    movienameurl = dict(zip(movies, moviurl))
    return render(request, 'movies/similar_moviepage.html', {'movienameurl': movienameurl, 'movies': movies})


def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['movieId', 'title','genres'])

    found_entries = Movies.objects.filter(entry_query)
    return render(request, 'movies/search_results.html', {'query_string': query_string, 'found_entries': found_entries })