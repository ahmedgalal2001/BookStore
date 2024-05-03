from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    image = models.URLField()
    price = models.FloatField()
    genre = models.CharField(max_length=100, null=True)
    rating = models.FloatField(null=True)
    views = models.IntegerField(null=True)
    description = models.TextField()