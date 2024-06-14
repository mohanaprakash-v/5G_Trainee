from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

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
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists!")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exists!")
                return redirect('register')
            else:
                # creating a user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match!")
            return redirect('register')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirecting home page
        else:
            messages.info(request, 'Invalid Login Details!!')
            return redirect('login')
        
    return render(request, 'login.html')
