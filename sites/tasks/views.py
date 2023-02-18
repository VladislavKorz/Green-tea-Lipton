from django.shortcuts import render, redirect
from .models import Task, Column


def task_list(request):
    title = "Менеджер задач"
    columns = Column.objects.all()
    return render(request, 'tasks/task_list.html', {'title':title, 'columns': columns})

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})

def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task.objects.create(title=title, description=description)
        return redirect('task_detail', pk=task.pk)
    else:
        return render(request, 'tasks/task_form.html')

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('task_detail', pk=task.pk)
    else:
        return render(request, 'tasks/task_form.html', {'task': task})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')