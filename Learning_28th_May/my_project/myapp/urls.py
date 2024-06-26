from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('counter/', views.counter, name='counter'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('csrf-token/', views.csrf_token, name='csrf_token'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('profile/', views.profile, name='profile'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('delete_user/<str:username>/', views.delete_user, name='delete_user'),
    path('update_user/<str:username>/', views.update_user, name='update_user'),
]
