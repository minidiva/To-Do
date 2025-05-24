from django.urls import path
from .views import home
from .views import say_hello

urlpatterns = [
    path('home/', home, name='home'),
    path('hello/', say_hello, name='say_hello'),
]