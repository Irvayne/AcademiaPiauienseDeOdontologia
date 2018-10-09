from django.shortcuts import render
from core.models import Estatuto, Sobre, Noticia, Curso, Diretoria, Home, CadeiraFundadoresTitulares


def index(request):
	noticias = Noticia.objects.all()
	cursos = Curso.objects.all()

	if len(noticias) >= 3:
		ultimas_noticias = noticias[len(noticias) - 3 : len(noticias)]
	elif len(noticias) >= 2:
		ultimas_noticias = noticias[len(noticias) - 2 : len(noticias)]
	else:
		ultimas_noticias = noticias

	if len(cursos) >= 3:
		ultimos_cursos = cursos[len(cursos) - 3 : len(cursos)]
	elif len(cursos) >= 2:
		ultimos_cursos = cursos[len(cursos) - 2 : len(cursos)]
	else:
		ultimos_cursos = cursos
	
	ultimas_noticias.reverse()
	ultimos_cursos.reverse()

	sobre = Sobre.objects.get(id=1)
	home = Home.objects.get(id=1)

	return render(request, 'index.html', {'sobre': sobre, 'ultimas_noticias': ultimas_noticias, 'ultimos_cursos': ultimos_cursos, 'home': home})


def estatuto(request):
	estatuto = Estatuto.objects.get(id=1)
	return render(request, 'front_estatuto.html', {'estatuto': estatuto })


def diretorias(request):
	diretorias = Diretoria.objects.all()
	return render(request, 'front_diretorias.html', {'diretorias': diretorias})


def lista_noticias(request):
	noticias = Noticia.objects.all()
	lista_noticias = noticias
	lista_noticias.reverse()

	return render(request, 'front_noticias.html', {'noticias': lista_noticias})


def lista_cursos(request):
	cursos = Curso.objects.all()
	cursos.reverse()
	return render(request, 'front_cursos.html', {'cursos': cursos})


def detalha_noticia(request, id_noticia):
	noticia = Noticia.objects.get(id=id_noticia)
	return render(request, 'front_detalha_noticia.html', {'noticia': noticia})


def detalha_curso(request, id_curso):
	curso = Curso.objects.get(id=id_curso)
	return render(request, 'front_detalha_curso.html', {'curso': curso})


def lista_cadeiras_fundadores(request):
	cadeiras_fundadores = CadeiraFundadoresTitulares.objects.all()
	return render(request, 'front_lista_cadeiras_fundadores.html', {'cadeiras': cadeiras_fundadores})