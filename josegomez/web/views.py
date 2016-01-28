from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Buenas! Bienvenido a mi web personal!")