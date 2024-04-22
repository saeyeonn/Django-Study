from django.http import HttpResponse
from django.shortcuts import render

import datetime

def index(request):
    # return HttpResponse("<h1 style=\"color:blue\">Hello, world</h1>")
    return render(request, "hello/index.html")
    
def saeyeon(request):
    return HttpResponse("Hello, Saeyeon")

def cherry(request):
    return HttpResponse("Hello, Cherry")

def greet(request, name):
    # return HttpResponse(f"Hello, {name}!")
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()    
    })