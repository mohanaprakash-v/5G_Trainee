from django.contrib import admin
from .models import Feature, Publisher, Author, Book, Review, Store, Inventory

# Register your models here.
admin.site.register(Feature)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Store)
admin.site.register(Inventory)