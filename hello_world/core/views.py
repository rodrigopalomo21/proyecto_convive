from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)


#dame una serie de paginas que se llamen 

def home(request):
    return HttpResponse("Inicio")

def about(request):
    return HttpResponse("Historia")

def services(request):
    return HttpResponse("Servicios")

def store(request):
    return HttpResponse("Visítanos")

def contact(request):
    return HttpResponse("Contacto")

def blog(request):
    return HttpResponse("Blog")

def sample(request):
    return HttpResponse("Sample")
core/urls.py
from django.contrib import admin
from django.urls import path
from core import views
