from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.render_task_creating, name='task_form'),
    path('list/', views.render_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/fetch/', views.task_fetch, name='task_get'),
    path('task/complete/', views.task_toggle, name='task_toggle')
]