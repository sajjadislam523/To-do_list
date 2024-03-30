from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm


def home(request):
    return render(request, 'home.html')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'add_tasks.html', context)

def show_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=False)
    context = {'tasks': tasks}
    return render(request, 'show_tasks.html', context)

def delete_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.delete()
    return redirect('show_tasks')

def edit_task(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'edit_task.html', context)

def mark_completed(request, pk):
    task = get_object_or_404(TaskModel, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')

def completed_tasks(request):
    tasks = TaskModel.objects.filter(is_completed=True)
    context = {'tasks': tasks}
    return render(request, 'completed_tasks.html', context)