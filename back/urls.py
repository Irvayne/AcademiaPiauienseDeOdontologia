
from django.contrib import admin
from back import views
from django.urls import path, include


urlpatterns = [
    path('admin/home/', views.home, name='home'),
    path('admin/home/editar', views.home_editar, name='home_editar'),
    path('admin/estatuto', views.estatuto, name='estatuto'),
    path('admin/estatuto/editar', views.estatuto_editar, name='estatuto_editar'),
    path('admin/noticias', views.noticias, name='noticias'),
    path('admin/noticias/cadastrar', views.noticias_cadastrar, name='noticias_cadastrar'),
    path('admin/noticias/<int:noticia_id>/remover', views.noticias_remover, name='noticias_remover'),
    path('admin/noticias/<int:noticia_id>/editar', views.noticias_editar, name='noticias_editar'),
    path('admin/diretorias', views.diretorias, name='diretorias'),
    path('admin/diretorias/cadastrar', views.diretorias_cadastrar, name='diretorias_cadastrar'),
    path('admin/diretorias/<int:diretoria_id>/remover', views.diretorias_remover, name='diretorias_remover'),
    path('admin/diretorias/<int:diretoria_id>/editar', views.diretorias_editar, name='diretorias_editar'),
    path('admin/membros', views.membros, name='membros'),
    path('admin/membros/cadastrar', views.membros_cadastrar, name='membros_cadastrar'),
    path('admin/membros/<int:membro_id>/remover', views.membros_remover, name='membros_remover'),
    path('admin/membros/<int:membro_id>/editar', views.membros_editar, name='membros_editar'),
    path('admin/cursos', views.cursos, name='cursos'),
    path('admin/cursos/cadastrar', views.cursos_cadastrar, name='cursos_cadastrar'),
    path('admin/cursos/<int:curso_id>/remover', views.cursos_remover, name='cursos_remover'),
    path('admin/cursos/<int:curso_id>/editar', views.cursos_editar, name='cursos_editar'),
    path('admin/cadeiras', views.cadeiras, name='cadeiras'),
    path('admin/cadeiras/cadastrar', views.cadeiras_cadastrar, name='cadeiras_cadastrar'),
    path('admin/cadeiras/<int:cadeira_id>/remover', views.cadeiras_remover, name='cadeiras_remover'),
    path('admin/cadeiras/<int:cadeira_id>/editar', views.cadeiras_editar, name='cadeiras_editar'),
    path('admin/sobre', views.sobre, name='sobre'),
    path('admin/sobre/editar', views.sobre_editar, name='sobre_editar'),
    path('admin/email/enviar', views.email_enviar, name='email_enviar'),
    path('admin/cadeira/fundadores', views.cadeira_fundadores, name='cadeira_fundadores'),
    path('admin/cadeira/fundadores/cadastrar', views.cadeira_fundadores_cadastrar, name='cadeira_fundadores_cadastrar'),
    path('admin/cadeira/fundadores/<int:cadeira_fundadores_id>/remover', views.cadeira_fundadores_remover, name='cadeira_fundadores_remover'),
    path('admin/cadeira/fundadores/<int:cadeira_fundadores_id>/editar', views.cadeira_fundadores_editar, name='cadeira_fundadores_editar'),

   ]
