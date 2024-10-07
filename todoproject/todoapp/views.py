from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task
            return redirect('/')  # Redirect to home after adding task

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/task_list.html', context)

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()  # Delete the task
    return redirect('/')  # Redirect to home after deletion

