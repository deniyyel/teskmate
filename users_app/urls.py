from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    #path('', views.todolist, name='todolist'),
    #path('', views.index, name='index'),  # This line defines the 'index' URL pattern
    path('register/', views.register, name='register'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    
  
    # Additional URL patterns...
]  # Closing square bracket

    #path('delete/', views.deletingTask, name='delete'),
