# drf_app/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from .models import Person
from .serializers import PeopleSerializer

# Standard Django view
def index_html(request):
    return HttpResponse("Hello, World!")

# API view
@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
        'course_name': 'Python',
        'learn': ['Django', 'Tornado', 'FastApi'],
        'course_provider': 'Scalar'
    }

    if request.method == 'GET':
        print("We got a GET method")
        return Response(courses)
    elif request.method == 'POST':
        print("We got a POST method")
        data = request.data
        print(data)
        return Response(courses)
    elif request.method == 'PUT':
        print("We got a PUT method")
        return Response(courses)

# ---SERIALIZERS CONCEPT---
# CRUD Methods using Serializers
@api_view(['GET', 'POST'])
def person(request):
    # Checking whether it is GET method  
    if request.method == 'GET':
        # Getting all the person datas form DB in 'Person' class
        objs = Person.objects.all()   # 'all' --- means as a set = [1,2,3,4,5] 
        # Passing 'many' if the data is more than one 
        serializer = PeopleSerializer(objs, many = True)
        return Response(serializer.data)  # returns a LIST
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    # ERROR Response
    return Response(serializer.errors)
