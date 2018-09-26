
from django.contrib import admin
from back import views
from django.urls import path, include


urlpatterns = [
    path('admin/home/', views.home, name='home'),
    path('admin/estatuto', views.estatuto, name='estatuto'),
    path('admin/estatuto/editar', views.estatuto_editar, name='estatuto_form'),
    path('admin/noticias', views.noticias, name='noticias'),
    path('admin/noticias/cadastrar', views.noticias_cadastrar, name='noticias_form'),
    path('admin/noticias/<int:noticia_id>/remover', views.noticias_remover, name='noticias_remover'),
    path('admin/diretorias', views.diretorias, name='diretorias'),
    path('admin/diretorias/cadastrar', views.diretorias_cadastrar, name='diretorias_form'),
    path('admin/diretorias/<int:diretoria_id>/remover', views.diretorias_remover, name='diretorias_remover'),
    path('admin/membros', views.membros, name='membros'),
    path('admin/membros/cadastrar', views.membros_cadastrar, name='membros_form'),
    path('admin/membros/<int:membro_id>/remover', views.membros_remover, name='membros_remover'),
    path('admin/cursos', views.cursos, name='cursos'),
    path('admin/cursos/cadastrar', views.cursos_cadastrar, name='cursos_form'),
    path('admin/cursos/<int:curso_id>/remover', views.cursos_remover, name='cursos_remover'),
    path('admin/cadeiras', views.cadeiras, name='cadeiras'),
    path('admin/cadeiras/cadastrar', views.cadeiras_cadastrar, name='cadeiras_form'),
    path('admin/cadeiras/<int:cadeira_id>/remover', views.cadeiras_remover, name='cadeiras_remover'),
    path('admin/sobre', views.sobre, name='sobre'),
    path('admin/sobre/editar', views.sobre_editar, name='sobre_form'),
   ]
