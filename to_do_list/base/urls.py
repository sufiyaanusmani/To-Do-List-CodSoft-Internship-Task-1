from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home-page'),
    path('delete/<int:delID>/', views.deleteTask, name='delete-task'),
    path('edit/<int:editID>/', views.editTask, name='edit-task'),
]
