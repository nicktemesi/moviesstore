from django.db import models
class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genre = models.CharField(max_length=50)
    

    def __str__(self):
        return f' Movie Title: {self.title}'
