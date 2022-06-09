from django.db import models


class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    image = models.ImageField(upload_to='movie_thumbnail',default='./movie_thumbnail/default.jpg')
    rating = models.FloatField()
    category =models.CharField(max_length=200, default='New Movies')

    def __str__(self):
        return self.name
