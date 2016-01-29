from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Buenas! Bienvenido a mi web personal!")

def hello(request):
	return HttpResponse("Buenas! Bienvenido al apartado hello!") 

def blog(request):
	return HttpResponse("Buenas! Bienvenido al apartado blog !") 

def post(request):
	return HttpResponse("Buenas! Bienvenido al apartado post !") 

def projects(request):
	return HttpResponse("Buenas! Bienvenido al apartado projects !") 

def aboutme(request):
	return HttpResponse("Buenas! Bienvenido al apartado aboutme !") 
