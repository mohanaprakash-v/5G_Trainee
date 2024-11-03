from django.contrib import admin
from .models import Feature, Publisher, Author, Book

# Register your models here.
admin.site.register(Feature)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)