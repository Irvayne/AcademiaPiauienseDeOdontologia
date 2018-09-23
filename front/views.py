from django.shortcuts import render
from core.models import Estatuto, Sobre, Noticia, Curso, Diretoria


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
		
	sobre = Sobre.objects.get(id=1)
	return render(request, 'index.html', {'sobre': sobre, 'ultimas_noticias': ultimas_noticias, 'ultimos_cursos': ultimos_cursos})


def estatuto(request):
	estatuto = Estatuto.objects.get(id=1)
	return render(request, 'front_estatuto.html', {'estatuto': estatuto })


def diretorias(request):
	diretorias = Diretoria.objects.get(id=3)
	return render(request, 'front_diretorias.html', {'diretorias': diretorias})