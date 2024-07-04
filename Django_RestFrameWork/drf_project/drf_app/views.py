from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Person
from .serializers import PeopleSerializer, LoginSerializer

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
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    # Checking whether it is GET method  
    if request.method == 'GET':
        # Getting all the person datas form DB in 'Person' class
        objs = Person.objects.filter(color__isnull = False)  # 'all' --- means as a set = [1,2,3,4,5] #give us the empty queryset object
        # Passing 'many' if the data is more than one 
        serializer = PeopleSerializer(objs, many=True)
        return Response(serializer.data)  # returns a LIST
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data=data)  #converts into query set
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # ERROR Response
        return Response(serializer.errors)
    elif request.method == 'PUT':  # PUT Method doesn't allow partial updation
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # ERROR Response
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        try:
            person = Person.objects.get(id=data["id"])
        except Person.DoesNotExist:
            return Response({"error": "Person not found"}, status=404)
        
        # Checking whether 'name' field is available in data list
        if 'name' in data:
            person.name = data["name"]

        serializer = PeopleSerializer(person, data=data, partial=True)  # PATCH method allows partial updation

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # ERROR Response
        return Response(serializer.errors, status = 400)
    
    else:
        data = request.data
        person = Person.objects.get(id=data["id"])
        person.delete()
        return Response({"message" : "Person is Deleted"})
    
@api_view(['POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if serializer.is_valid():
        data = serializer.validated_data
        return Response({"message" : "Success"})
    
    return Response(serializer.errors)