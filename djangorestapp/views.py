from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("This is djangorestapp response")

def demo(request):
    return HttpResponse("This is djangorestapp demo response")