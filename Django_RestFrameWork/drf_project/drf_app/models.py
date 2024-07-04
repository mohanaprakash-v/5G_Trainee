from django.db import models

# Create your models here.


class Color(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name
    
    

class Person(models.Model):
    # adding related name so that we can add a reverse mapping to it
    color = models.ForeignKey(Color, on_delete = models.CASCADE, null= True, blank= True, related_name= "color")
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    sports = models.CharField(max_length=200, null=True)