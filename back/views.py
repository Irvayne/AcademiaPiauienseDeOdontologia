from django.shortcuts import render, redirect
from core.models import Estatuto, Noticia, Diretoria, Membro, Curso, Cadeira, Sobre

def home(request):
	return render(request, 'home.html')

def estatuto(request):
	try:
		estatuto = Estatuto.objects.get(id=1)
	except:
		estatuto = Estatuto(conteudo='Digite o conteudo do estatuto')	
		estatuto.save()
	return render(request, 'estatuto.html', {'estatuto': estatuto})

def estatuto_form(request):
	estatuto = Estatuto.objects.get(id=1)
	if request.method == 'POST':
		estatuto.conteudo = request.POST['estatuto_conteudo']
		estatuto.save()
		return redirect('estatuto')
	else:
		return render(request, 'estatuto_form.html', {'estatuto': estatuto })


def noticias(request):
	return render(request, 'noticias.html', {'noticias': Noticia.objects.all()})

def noticias_form(request):
	if request.method == 'POST':
		noticia = Noticia(titulo=request.POST['titulo'], subtitulo=request.POST['subtitulo'], conteudo=request.POST['conteudo'])
		noticia.save()
		return redirect('noticias')
	else:
		return render(request, 'noticias_form.html')

def diretorias(request):
	try:
		diretorias = Diretoria.objects.all()
	except:
		diretorias = []
	return render(request, 'diretorias.html', {'diretorias': diretorias})

def diretorias_form(request):
	if request.method == 'POST':
		diretoria = Diretoria(nome=request.POST['nome'], descricao=request.POST['descricao'])
		diretoria.save()
		return redirect('diretorias')
	else:
		return render(request, 'diretorias_form.html')

def membros(request):
	try:
		membros = Membro.objects.all()
	except:
		membros = []
	return render(request, 'membros.html', {'membros': membros})

def membros_form(request):
	if request.method == 'POST':
		membro = Membro(nome=request.POST['nome'], descricao=request.POST['descricao'])
		membro.save()
		return redirect('membros')
	else:
		return render(request, 'membros_form.html')

def cursos(request):
	try:
		cursos = Curso.objects.all()
	except:
		cursos = []
	return render(request, 'cursos.html', {'cursos': cursos})

def cursos_form(request):
	if request.method == 'POST':
		curso = Curso(nome=request.POST['nome'], descricao=request.POST['descricao'], conteudo=request.POST['conteudo'])
		curso.save()
		return redirect('cursos')
	else:
		return render(request, 'cursos_form.html')

def cadeiras(request):
	try:
		cadeiras = Cadeira.objects.all()
	except:
		cadeiras = []
	return render(request, 'cadeiras.html', {'cadeiras': cadeiras})

def cadeiras_form(request):
	if request.method == 'POST':
		cadeira = Cadeira(nome=request.POST['nome'], descricao=request.POST['descricao'])
		cadeira.save()
		return redirect('cadeiras')
	else:
		return render(request, 'cadeiras_form.html')

def sobre(request):
	try:
		sobre = Sobre.objects.get(id=1)
	except:
		sobre = Sobre(conteudo="")
		sobre.save()

	return render(request, 'sobre.html', {'sobre': sobre })

def sobre_form(request):
	sobre = Sobre.objects.get(id=1)
	if request.method == 'POST':
		sobre.conteudo = request.POST['conteudo']
		sobre.save()
		return redirect('sobre')
	else: 	
		return render(request, 'sobre_form.html', {'sobre': sobre })


