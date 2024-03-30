from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_tasks/', views.add_task, name='add_tasks'),
    path('show_tasks/', views.show_tasks, name='show_tasks'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('mark_completed/<int:pk>/', views.mark_completed, name='mark_completed'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
]