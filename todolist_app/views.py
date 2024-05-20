from django.shortcuts import render, redirect
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
