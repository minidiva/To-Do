from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Привет, это главная страница!")

def calculate():
    x = 1
    y = 2
    return x + y

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'ALAN'})
