from django.contrib import admin
from front import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('estatuto/', views.estatuto, name='front_estatuto'),
    path('diretoria/lista/', views.diretorias, name='front_diretoria'),
    path('noticia/lista/', views.lista_noticias, name='front_noticias'),
    path('curso/lista/', views.lista_cursos, name='front_cursos'),
]