from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todolist_app.models import Tasklist
from todolist_app.form import Taskform
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

#  views Creation here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            task = form.save(commit=False)
            task.manage= request.user
            task.save()
        messages.success(request,('New task has been added')) 
        return redirect('todolist')
    else:
        all_tasks = Tasklist.objects.filter(manage=request.user)  # fetching all tasks from the models
        paginator = Paginator(all_tasks, 5)  # Show 5 tasks per page
        
        page = request.GET.get('pg')
        try:
            tasks = paginator.page(page)
        except PageNotAnInteger:
            tasks = paginator.page(1)
        except EmptyPage:
            tasks = paginator.page(paginator.num_pages)
        
        return render(request, 'todolist.html', {'tasks': tasks})
        
        #return render(request, 'todolist.html', {'all_task': all_task})
        
@login_required
def delete_task(request, task_id):
     task = Tasklist.objects.get(pk=task_id)
     if task.manage == request.user:
         task.delete()
     else:
        messages.error(request,(' Access restricted, you do not have access to this page! ')) 
     
     return redirect('todolist')
 
@login_required
def edit_task(request, task_id):
    print(f"Received request to edit task with ID: {task_id}")  # Debugging statement
    if request.method == "POST":
        task = Tasklist.objects.get(pk=task_id)
        form = Taskform(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, 'Task Edited')
        return redirect('todolist')
    else:
        task_obj = get_object_or_404(Tasklist, pk=task_id)
        print(f"Fetched task: {task_obj}")  # Debugging statement
        return render(request, 'edit.html', {'task_obj': task_obj})  # Use 'task_obj' as the context variable name
    

@login_required
def completed_task(request, task_id):
    task = get_object_or_404(Tasklist, pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
       # messages.success(request, 'Task marked as completed.')
    else:
        messages.error(request, 'Access restricted. You do not have permission to perform this action.')
    return redirect('todolist')

    


@login_required
def pending_task(request, task_id):
    task = get_object_or_404(Tasklist, pk=task_id)
    if task.manage == request.user:
        task.done = False
        task.save()
        #messages.success(request, 'Task marked as pending.')
    else:
        messages.error(request, 'Access restricted. You do not have permission to perform this action.')
    return redirect('todolist')
def index(request):
    context ={
        'index_text':"welcome to taskmate.",
        }
    return render(request, 'index.html', context)

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
