from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse  # clase que me permite ejecutar una respuesta HTTP


def index(request):
    return HttpResponse("Hola socitos")
    