from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def counter(request):
    words = request.POST['count']
    text_length = len(words.split())
    return render(request, 'counter.html', {'length': text_length})


# When a request matches the root URL of the project (i.e., http://127.0.0.1:8000/), Django first checks the project-level urlpatterns and sees that it includes the myapp/urls.py for this URL. It then checks the app-level urlpatterns in myapp/urls.py, finds the pattern path('', views.home, name='home'), and calls the home view function from myapp/views.py.