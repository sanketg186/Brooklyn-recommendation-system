from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pref/', views.pref, name='pref'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^rate/$', views.rate, name='rate'),
    url(r'^similar_movie/$', views.similar_movie, name='similar_movie'),
    url(r'^search/$', views.search, name='search'),
    url(r'^rated_movies/$', views.rated_movies, name='rated_movies'),
]
