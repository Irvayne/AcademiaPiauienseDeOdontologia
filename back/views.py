from django.shortcuts import render, redirect
from core.models import Estatuto, Noticia, Diretoria, Membro, Curso, Cadeira, Sobre
from django.core.files.storage import FileSystemStorage

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
	noticias = Noticia.objects.all()
	lista_noticias = noticias
	lista_noticias.reverse()
	return render(request, 'noticias.html', {'noticias': lista_noticias})

def noticias_form(request):
	if request.method == 'POST':
		if request.FILES['imagem']:
			imagem = request.FILES['imagem']
			fs = FileSystemStorage()
			filename = fs.save(imagem.name, imagem)
			uploaded_file_url = fs.url(filename)
			noticia = Noticia(titulo=request.POST['titulo'], subtitulo=request.POST['subtitulo'], conteudo=request.POST['conteudo'], imagem=uploaded_file_url)
		else:
			noticia = Noticia(titulo=request.POST['titulo'], subtitulo=request.POST['subtitulo'], conteudo=request.POST['conteudo'], imagem=None)
		noticia.save()
		return redirect('noticias')
	else:
		return render(request, 'noticias_form.html')

def noticias_remover(request, noticia_id):
	noticia = Noticia.objects.get(id=noticia_id)
	noticia.delete()
	return redirect('noticias')


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

def diretorias_remover(request, diretoria_id):
	diretoria = Diretoria.objects.get(id=diretoria_id)
	diretoria.delete()
	return redirect('diretorias')

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

def membros_remover(request, membro_id):
	membro = Membro.objects.get(id=membro_id)
	membro.delete()
	return redirect('membros')

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

def cursos_remover(request, curso_id):
	curso = Curso.objects.get(id=curso_id)
	curso.delete()
	return redirect('cursos')

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

def cadeiras_remover(request, cadeira_id):
	cadeira = Cadeira.objects.get(id=cadeira_id)
	cadeira.delete()
	return redirect('cadeiras')

def sobre(request):
	try:
		sobre = Sobre.objects.get(id=1)
	except:
		sobre = Sobre(conteudo="")
		sobre.save()

	return render(request, 'sobre.html', {'sobre': sobre })

def sobre_form(request):
	sobre = Sobre.objects.get(id=1)
	if request.method == 'POST' and request.FILES['imagem']:
		imagem = request.FILES['imagem']
		fs = FileSystemStorage()
		filename = fs.save(imagem.name, imagem)
		uploaded_file_url = fs.url(filename)
		sobre.titulo = request.POST['titulo']
		sobre.conteudo = request.POST['conteudo']
		sobre.imagem = uploaded_file_url
		sobre.save()
		return redirect('sobre')
	else: 	
		return render(request, 'sobre_form.html', {'sobre': sobre })


