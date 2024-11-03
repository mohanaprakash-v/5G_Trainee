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



#------------------------------------- PREFETCH AND SELECT RELATED QUERY (START) ---------------------------

from django.shortcuts import render
from .models import Book

# TO DISPLAY BOOK NAMES WITH PUBLISHER


def book_list_with_publisher(request):

    # Using select_related to fetch publisher information in a single query
    books = Book.objects.select_related('publisher').all()
    return render(request, 'books/book_list_with_publisher.html', {'books': books})


# TO DISPLAY BOOKS WITH AUTHOR NAMES

def book_list_with_authors(request):

    # Using prefetch_related to fetch authors in a separate query and attach them to books
    books = Book.objects.prefetch_related('authors').all()
    return render(request, 'books/book_list_with_authors.html', {'books': books})

# TO DISPLAY ALL BOOKS WITH BOTH PUBLISHERS AND AUTHORS

def book_list_with_publisher_and_authors(request):

    # Using select_related and prefetch_related together
    books = Book.objects.select_related('publisher').prefetch_related('authors').all()
    return render(request, 'books/book_list_with_publisher_and_authors.html', {'books': books})



#------------------------------------- PREFETCH AND SELECT RELATED QUERY (END) -----------------------------

def index(request):
    # features = Feature.objects.all()
    return render(request, 'index.html')   # {'features': features}

# def counter(request):
#     words = request.POST['count']
#     text_length = len(words.split())
#     return render(request, 'counter.html', {'length': text_length})

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
        context = {}

        if username == '' or password == '':
            context['errmsg'] = 'Fields are Not Empty'
            return render(request, 'login.html', context)
        else:
            user = authenticate(username=username , password=password)
            print(user.password, user.is_superuser)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                context['errmsg'] = "Invalid username and password"
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')





    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
        
    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         auth_login(request, user)
    #         return redirect('home')
    #     else:
    #         messages.info(request, 'Invalid Login Details!!')
    #         return redirect('login')
    # return render(request, 'login.html')

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

def profile_page(request):
    users = User.objects.all()
    return render(request, 'profile.html', {'users': users})

@csrf_exempt
@require_POST
def csrf_token(request):
    try:
        data = json.loads(request.body)

        # Get username and password from the request
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log In User
            auth_login(request, user)
            
            # Generating CSRF Token
            csrf_token = get_token(request)
            
            return JsonResponse({'csrfToken': csrf_token})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET", "POST"])
def update_user(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if username and username != user.username:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
                return redirect('update_user', username=user.username)
            else:
                user.username = username
        
        if email:
            user.email = email
        
        if password:
            user.set_password(password)
        
        user.save()
        return redirect('profile_page')
    
    return render(request, 'update_user.html', {'user': user})

@require_http_methods(["GET", "POST"])
def delete_user(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.method == "POST":
        user.delete()
        return redirect('home')
    
    return render(request, 'delete_user.html', {'user': user})