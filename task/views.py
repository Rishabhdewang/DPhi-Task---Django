from django.shortcuts import render
from django.http import HttpResponse 

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PlantSerializer
from .models import Plant 
# Create your views here.
@api_view(['GET'])
def index(request):

    return Response("Hello ,This is homepage")

@api_view(['POST'])
def signup(request):
    print('HEllo World')

    return HttpResponse("SIgnup")

def login(request):
    return HttpResponse("SIgnup")
 
@api_view(['GET'])
def allplants(request):
    plants = Plant.objects.all()
    # serializer = PlantSerializer(Plant, many='true')
    return Response(plants)

def addplant(request):
    return HttpResponse("SIgnup")

def viewplant(request):
    return HttpResponse("SIgnup")

def placeorder(request):
    return HttpResponse("SIgnup")

def vieworder(request):
    return HttpResponse("SIgnup")