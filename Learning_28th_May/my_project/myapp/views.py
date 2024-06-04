from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):

    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'Naresh'
    feature1.details = 'Devops Engineer'
    feature1.is_true = True    

    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'Vijay'
    feature2.details = 'UI/UX Designer'
    feature2.is_true = True

    feature3 = Feature()
    feature3.id = 3
    feature3.name = 'Mohan'
    feature3.details = 'Software Developer'
    feature3.is_true = False

    features = [feature1, feature2, feature3]

    return render(request,'index.html', {'features': features})

def counter(request):
    words = request.POST['count']
    text_length = len(words.split())
    return render(request, 'counter.html', {'length': text_length})

# When a request matches the root URL of the project (i.e., http://127.0.0.1:8000/), Django first checks the project-level urlpatterns and sees that it includes the myapp/urls.py for this URL. It then checks the app-level urlpatterns in myapp/urls.py, finds the pattern path('', views.home, name='home'), and calls the home view function from myapp/views.py.