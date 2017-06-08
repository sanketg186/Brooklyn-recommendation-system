from django.contrib import admin
from .models import GenreSelect, UserRating,Movies
# Register your models here.

admin.site.register(GenreSelect)
admin.site.register(UserRating)
admin.site.register(Movies)