from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todolist_app.models import Tasklist
from todolist_app.form import Taskform
from django.contrib import messages


# Create your views here.
def todolist(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('New task has been added')) 
        return redirect('todolist')
    else:
        all_task = Tasklist.objects.all # fatching all file from the models 
        return render(request, 'todolist.html', {'all_task': all_task})
    
def delete_task(reques, task_id):
     task = Tasklist.objects.get(pk=task_id)
     task.delete()
     
     return redirect('todolist')
 
def edit_task(request, task_id):
    print(f"Received request to edit task with ID: {task_id}")  # Debugging statement
    if request.method == "POST":
        messages.success(request, 'Task Edited')
        return redirect('todolist')
    else:
        task_obj = get_object_or_404(Tasklist, pk=task_id)
        print(f"Fetched task: {task_obj}")  # Debugging statement
        return render(request, 'edit.html', {'task_obj': task_obj})  # Use 'task_obj' as the context variable name
    
     
def contact(request):
    context ={
        'contact_text':"welcome to contact.",
        }
    return render(request, 'contact.html', context)

def about(request):
    context ={
        'about_text':"weolcome to about.",
        }
    return render(request, 'about.html', context)
