from django.db import models

# Create your models here.

class Feature(models.Model):
    
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    published_date = models.DateField(null=True)
    genre = models.CharField(max_length=50, null=True, blank=True)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()

class Store(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, through='Inventory')

class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    stock = models.IntegerField()