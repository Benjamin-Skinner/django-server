from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse

# Create your views here.

response = JsonResponse({
    "chai": "Egypt",
    "chungus": "America"
})

def index(request):
    return response
