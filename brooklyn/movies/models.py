from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.


class GenreSelect(models.Model):
    user = models.OneToOneField(User)
    Action = models.IntegerField(default=0)
    Adventure = models.IntegerField(default=0)
    Animation = models.IntegerField(default=0)
    Children = models.IntegerField(default=0)
    Comedy = models.IntegerField(default=0)
    Crime = models.IntegerField(default=0)
    Documentary = models.IntegerField(default=0)
    Drama = models.IntegerField(default=0)
    Fantasy = models.IntegerField(default=0)
    FilmNoir = models.IntegerField(default=0)
    Horror = models.IntegerField(default=0)
    Musical = models.IntegerField(default=0)
    Mystery = models.IntegerField(default=0)
    Romance = models.IntegerField(default=0)
    SciFi = models.IntegerField(default=0)
    Thriller = models.IntegerField(default=0)
    War = models.IntegerField(default=0)
    Western = models.IntegerField(default=0)


class UserRating(models.Model):
    class Meta:
        unique_together = (('user', 'movie_title'),)
    user = models.CharField(max_length=250)
    movie_title = models.CharField(max_length=250, default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.rating)+self.movie_title


class Movies(models.Model):
    movieId = models.IntegerField(default=0)
    title = models.CharField(max_length=500)
    genres = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)