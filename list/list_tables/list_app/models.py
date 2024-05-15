from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):

        return '{}'.format(self.title)


class BookAuthor(models.Model):
    author = models.CharField(max_length=200)