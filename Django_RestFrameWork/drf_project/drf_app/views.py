from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

from drf_app.models import Person
from drf_app.serializers import PeopleSerializer

# Create your views here.

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
