
from django.contrib import admin
from back import views
from django.urls import path, include


urlpatterns = [
    path('admin/home/', views.home, name='home'),
    path('admin/estatuto', views.estatuto, name='estatuto'),
    path('admin/estatuto/editar', views.estatuto_editar, name='estatuto_editar'),
   ]
