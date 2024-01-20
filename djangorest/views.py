from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("This is first project")
    return render(request,'base.html',{'name':'Sai'})

def demo(request):
    # return HttpResponse("This is another response demo")
    return render(request,'demo.html',{'name':'Sai'})