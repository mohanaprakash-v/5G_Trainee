from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request,'index.html', {'features': features})

def counter(request):
    words = request.POST['count']
    text_length = len(words.split())
    return render(request, 'counter.html', {'length': text_length})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            pass

    return render(request, 'register.html')

# When a request matches the root URL of the project (i.e., http://127.0.0.1:8000/), Django first checks the project-level urlpatterns and sees that it includes the myapp/urls.py for this URL. It then checks the app-level urlpatterns in myapp/urls.py, finds the pattern path('', views.home, name='home'), and calls the home view function from myapp/views.py.