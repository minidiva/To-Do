from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Task
import json

def render_task_creating(request):
    return render(request, 'task.html')

def render_list(request):
    return render(request, 'list.html')

def task_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            task = Task.objects.create(
                title=data.get('title'),
                completed=data.get('completed', False)
            )
            return JsonResponse({
                'id': task.id, 
                'title': task.title, 
                'completed': task.completed
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def task_toggle(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            task_id = data.get('id')
            try:
                task = Task.objects.get(pk=task_id)
                task.completed = not task.completed
                task.save()
                return JsonResponse({'id': task.id, 'title': task.title, 'completed': task.completed})
            except Task.DoesNotExist:
                return JsonResponse({'error': 'Task not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def task_fetch(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        task_list = [{'id': task.id, 'title': task.title, 'completed': task.completed} for task in tasks]
        return JsonResponse({'tasks': task_list})
    return JsonResponse({'error': 'Invalid request method'}, status=405)