
from django.contrib import admin
from back import views
from django.urls import path, include


urlpatterns = [
    path('admin/home/', views.home, name='home'),
    path('admin/estatuto', views.estatuto, name='estatuto'),
    path('admin/estatuto/editar', views.estatuto_form, name='estatuto_form'),
    path('admin/noticias', views.noticias, name='noticias'),
    path('admin/noticias/editar', views.noticias_form, name='noticias_form'),
    path('admin/diretorias', views.diretorias, name='diretorias'),
    path('admin/diretorias/editar', views.diretorias_form, name='diretorias_form'),
    path('admin/membros', views.membros, name='membros'),
    path('admin/membros/editar', views.membros_form, name='membros_form'),
    path('admin/cursos', views.cursos, name='cursos'),
    path('admin/cursos/editar', views.cursos_form, name='cursos_form'),
    path('admin/cadeiras', views.cadeiras, name='cadeiras'),
    path('admin/cadeiras/editar', views.cadeiras_form, name='cadeiras_form'),
    path('admin/sobre', views.sobre, name='sobre'),
    path('admin/sobre/editar', views.sobre_form, name='sobre_form'),
   ]
