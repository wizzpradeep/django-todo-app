from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoView.as_view(), name='todo'),
    path('clear/', views.clear_all, name='clear_all'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),    
]
