
from django.contrib import admin
from back import views
from django.urls import path, include


urlpatterns = [
    path('admin/home/', views.home, name='home'),
    path('admin/estatuto', views.estatuto, name='estatuto'),
    path('admin/estatuto/editar', views.estatuto_form, name='estatuto_form'),
    path('admin/noticias', views.noticias, name='noticias'),
    path('admin/noticias/editar', views.noticias_form, name='noticias_form'),
   ]
