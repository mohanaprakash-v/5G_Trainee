from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    #---main/root url path---- Here index means function
    path('counter', views.counter, name='counter')
]