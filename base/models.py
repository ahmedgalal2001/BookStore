import random
import string

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20,unique=True)

class ISBN(models.Model):
    ISBN = models.CharField(max_length=13  , primary_key=True,serialize=False,verbose_name="ISBN" , validators=[])

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    image = models.URLField()
    price = models.FloatField()
    genre = models.CharField(max_length=100, null=True)
    rating = models.FloatField(null=True)
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(null=True)
    description = models.TextField()

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# @staticmethod
# @receiver(post_save, sender='base.Book')
# def create_isbn(sender, instance, created, **kwargs):
#     if created:
#         isbn = ''.join(random.choices(string.ascii_uppercase + string.digits, k=13))
#         instance.ISBN = isbn
#         instance.save()