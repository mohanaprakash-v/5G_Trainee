#users/urls.py

from django.urls import path
from . import views
from users.views import csrf_token


urlpatterns = [
    # path('login/', views.login_view, name='login'),
    path('csrf_token/', csrf_token, name='csrf_token'),
]