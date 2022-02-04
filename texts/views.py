from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the index :)")