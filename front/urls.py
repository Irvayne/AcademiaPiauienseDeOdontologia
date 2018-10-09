from django.contrib import admin
from front import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('estatuto/', views.estatuto, name='front_estatuto'),
    path('diretoria/lista/', views.diretorias, name='front_diretoria'),
    path('noticia/lista/', views.lista_noticias, name='front_noticias'),
    path('noticia/detalha/<int:id_noticia>/', views.detalha_noticia, name='front_detalha_noticia'),
    path('curso/lista/', views.lista_cursos, name='front_cursos'),
    path('curso/detalha/<int:id_curso>/', views.detalha_curso, name='front_detalha_curso'),
    path('cadeira/lista/', views.lista_cadeiras_fundadores, name='front_cadeiras_fundadores'),
]