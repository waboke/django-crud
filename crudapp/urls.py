from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('add-user', views.AddUser, name='add-user'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    
]