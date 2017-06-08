from .models import Movies
import csv
with open('D:/pilot_project/brooklyn/movies/ml-latest-small/movies.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        created = Movies.objects.get_or_create(movieId=row[0], title=row[1], genres=row[2])