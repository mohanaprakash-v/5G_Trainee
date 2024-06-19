from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_http_methods
import json
from .models import Feature

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
            return redirect('home')
        else:
            messages.info(request, 'Invalid Login Details!!')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('home')

def profile(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not (username and email and password):
            return JsonResponse({'error': 'All fields are required.'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists.'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists.'}, status=400)
    
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return JsonResponse({'message': 'User successfully inserted!'})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# def profiles_page(request):
#     users = User.objects.all()
#     return render(request, 'profiles.html', {'users': users})


def profile_page(request):
    users = User.objects.all()
    return render(request, 'profile.html', {'users': users})


@csrf_exempt
@require_POST
def get_csrf_token(request):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            csrf_token = get_token(request)
            return JsonResponse({'csrfToken': csrf_token})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# @csrf_exempt
# @require_POST
# def profiles(request):
#     try:
#         data = json.loads(request.body)
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')

#         if not (username and email and password):
#             return JsonResponse({'error': 'All fields are required.'}, status=400)

#         if User.objects.filter(username=username).exists():
#             return JsonResponse({'error': 'Username already exists.'}, status=400)

#         if User.objects.filter(email=email).exists():
#             return JsonResponse({'error': 'Email already exists.'}, status=400)
    
#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()
#         return JsonResponse({'message': 'User successfully inserted!'})
#     except json.JSONDecodeError:
#         return JsonResponse({'error': 'Invalid JSON'}, status=400)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# def profiles_page(request):
#     users = User.objects.all()
#     return render(request, 'profiles.html', {'users': users})

# @csrf_exempt
# @require_http_methods(["DELETE"])
# def delete_user(request, username):
#     try:
#         user = get_object_or_404(User, username=username)
#         user.delete()
#         return JsonResponse({'message': 'User deleted successfully.'})
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# @csrf_exempt
# @require_http_methods(["PUT"])
# def update_user(request, username):
#     try:
#         user = get_object_or_404(User, username=username)
#         data = json.loads(request.body)
#         user.email = data.get('email', user.email)
#         password = data.get('password')
#         if password:
#             user.set_password(password)
#         user.save()
#         return JsonResponse({'message': 'User updated successfully.'})
#     except json.JSONDecodeError:
#         return JsonResponse({'error': 'Invalid JSON'}, status=400)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)
