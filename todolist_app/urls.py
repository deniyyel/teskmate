from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # Additional URL patterns...
]  # Closing square bracket

    #path('delete/', views.deletingTask, name='delete'),
