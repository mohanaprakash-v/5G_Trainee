from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('counter/', views.counter, name='counter'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
]
