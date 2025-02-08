# tasks/views.py

from django.shortcuts import render, redirect,get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
    return redirect('task_list')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle the completion status
    task.save()
    return redirect('task_list')


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    tasks = Task.objects.all()  # Fetch all tasks

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.save()
        return redirect('task_list')

    return render(request, 'tasks/edit_task.html', {'task': task, 'tasks': tasks})

