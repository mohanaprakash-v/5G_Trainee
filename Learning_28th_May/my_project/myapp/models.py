from django.db import models

# Create your models here.

class Feature(models.Model):
    
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)