from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def todolist(request):
    context ={
        'todolist_text':"weolcome to todolist.",
        }
    return render(request, 'todolist.html', context)

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
