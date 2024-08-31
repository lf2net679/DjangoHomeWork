# todo/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('update/<int:id>/', views.update_todo, name='update_todo'),
    path('delete/<int:id>/', views.delete_todo, name='delete_todo'),
    path('register/', views.register, name='register'),
    path('register_check/', views.register_check, name='register_check'),
    path('todo/check_name/', views.check_name, name='check_name'),
    path('travel/', views.travel, name='travel')
]
