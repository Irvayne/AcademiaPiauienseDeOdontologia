from django.shortcuts import render, redirect
from core.models import Estatuto, Noticia, Diretoria, Membro, Curso, Cadeira, Sobre, Home, CadeiraFundadoresTitulares
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	try:
		home = Home.objects.get(id=1)
	except:
		home = Home()
		home.save()
	return render(request, 'home.html', {'home': home})


@login_required
def home_editar(request):
	home = Home.objects.get(id=1)
	if request.method == 'POST':
		home.telefone = request.POST['telefone']
		home.email = request.POST['email']
		home.localizadao = request.POST['localizadao']
		home.save()
		return redirect('home')
	else:
		return render(request, 'home_editar.html', {'home': home})


@login_required
def estatuto(request):
	try:
		estatuto = Estatuto.objects.get(id=1)
	except:
		estatuto = Estatuto(conteudo='Digite o conteudo do estatuto')	
		estatuto.save()
	return render(request, 'estatuto.html', {'estatuto': estatuto})


@login_required
def estatuto_editar(request):
	estatuto = Estatuto.objects.get(id=1)
	if request.method == 'POST':
		estatuto.conteudo = request.POST['estatuto_conteudo']
		estatuto.save()
		return redirect('estatuto')
	else:
		return render(request, 'estatuto_editar.html', {'estatuto': estatuto })


@login_required
def noticias(request):
	noticias = Noticia.objects.all()
	lista_noticias = noticias
	lista_noticias.reverse()
	return render(request, 'noticias.html', {'noticias': lista_noticias})


@login_required
def noticias_cadastrar(request):
	if request.method == 'POST':
		imagem = request.FILES.get('imagem', False)
		if imagem:
			fs = FileSystemStorage()
			filename = fs.save(imagem.name, imagem)
			uploaded_file_url = fs.url(filename)
			noticia = Noticia(titulo=request.POST['titulo'], subtitulo=request.POST['subtitulo'], conteudo=request.POST['conteudo'], imagem=uploaded_file_url)
		else:
			noticia = Noticia(titulo=request.POST['titulo'], subtitulo=request.POST['subtitulo'], conteudo=request.POST['conteudo'], imagem=None)
		noticia.save()
		return redirect('noticias')
	else:
		return render(request, 'noticias_cadastrar.html')


@login_required
def noticias_editar(request, noticia_id):
	noticia = Noticia.objects.get(id=noticia_id)
	if request.method == 'POST':
		noticia.titulo = request.POST['titulo']
		noticia.subtitulo = request.POST['subtitulo']
		noticia.conteudo = request.POST['conteudo']
		imagem = request.FILES.get('imagem', False)
		if imagem:
			fs = FileSystemStorage()
			filename = fs.save(imagem.name, imagem)
			uploaded_file_url = fs.url(filename)
			noticia.imagem=uploaded_file_url
		noticia.save()
		return redirect('noticias')
	else:
		return render(request, 'noticias_editar.html', {'noticia': noticia})


@login_required
def noticias_remover(request, noticia_id):
	noticia = Noticia.objects.get(id=noticia_id)
	noticia.delete()
	return redirect('noticias')


@login_required
def diretorias(request):
	try:
		diretorias = Diretoria.objects.all()
	except:
		diretorias = []
	return render(request, 'diretorias.html', {'diretorias': diretorias})


@login_required
def diretorias_cadastrar(request):
	if request.method == 'POST':
		diretoria = Diretoria(nome=request.POST['nome'], descricao=request.POST['descricao'])
		diretoria.save()
		return redirect('diretorias')
	else:
		return render(request, 'diretorias_cadastrar.html')


@login_required
def diretorias_editar(request, diretoria_id):
	diretoria = Diretoria.objects.get(id=diretoria_id)
	if request.method == 'POST':
		diretoria.nome = request.POST['nome']
		diretoria.descricao = request.POST['descricao']
		diretoria.save()
		return redirect('diretorias')
	else:
		return render(request, 'diretorias_editar.html', {'diretoria':diretoria})


@login_required
def diretorias_remover(request, diretoria_id):
	diretoria = Diretoria.objects.get(id=diretoria_id)
	diretoria.delete()
	return redirect('diretorias')


@login_required
def membros(request):
	try:
		membros = Membro.objects.all()
	except:
		membros = []
	return render(request, 'membros.html', {'membros': membros})


@login_required
def membros_cadastrar(request):
	if request.method == 'POST':
		membro = Membro(nome=request.POST['nome'], descricao=request.POST['descricao'])
		membro.save()
		return redirect('membros')
	else:
		return render(request, 'membros_cadastrar.html')


@login_required
def membros_editar(request, membro_id):
	membro = Membro.objects.get(id=membro_id)
	if request.method == 'POST':
		membro.nome = request.POST['nome']
		membro.descricao = request.POST['descricao']
		membro.save()
		return redirect('membros')
	else:
		return render(request, 'membros_editar.html', {'membro': membro})


@login_required
def membros_remover(request, membro_id):
	membro = Membro.objects.get(id=membro_id)
	membro.delete()
	return redirect('membros')


@login_required
def cursos(request):
	try:
		cursos = Curso.objects.all()
	except:
		cursos = []
	return render(request, 'cursos.html', {'cursos': cursos})


@login_required
def cursos_cadastrar(request):
	if request.method == 'POST':
		curso = Curso(nome=request.POST['nome'], descricao=request.POST['descricao'], conteudo=request.POST['conteudo'])
		curso.save()
		return redirect('cursos')
	else:
		return render(request, 'cursos_cadastrar.html')


@login_required
def cursos_editar(request, curso_id):
	curso = Curso.objects.get(id=curso_id)
	if request.method == 'POST':
		curso.nome = request.POST['nome']
		curso.descricao = request.POST['descricao']
		curso.conteudo = request.POST['conteudo']
		curso.save()
		return redirect('cursos')
	else:
		return render(request, 'cursos_editar.html', {'curso': curso})


@login_required
def cursos_remover(request, curso_id):
	curso = Curso.objects.get(id=curso_id)
	curso.delete()
	return redirect('cursos')


@login_required
def cadeiras(request):
	try:
		cadeiras = Cadeira.objects.all()
	except:
		cadeiras = []
	return render(request, 'cadeiras.html', {'cadeiras': cadeiras})


@login_required
def cadeiras_cadastrar(request):
	if request.method == 'POST':
		cadeira = Cadeira(nome=request.POST['nome'], descricao=request.POST['descricao'])
		cadeira.save()
		return redirect('cadeiras')
	else:
		return render(request, 'cadeiras_cadastrar.html')


@login_required
def cadeiras_editar(request, cadeira_id):
	cadeira = Cadeira.objects.get(id=cadeira_id)
	if request.method == 'POST':
		cadeira.nome = request.POST['nome']
		cadeira.descricao = request.POST['descricao']
		cadeira.save()
		return redirect('cadeiras')
	else:
		return render(request, 'cadeiras_editar.html', {'cadeira': cadeira})


@login_required
def cadeiras_remover(request, cadeira_id):
	cadeira = Cadeira.objects.get(id=cadeira_id)
	cadeira.delete()
	return redirect('cadeiras')


@login_required
def sobre(request):
	try:
		sobre = Sobre.objects.get(id=1)
	except:
		sobre = Sobre(conteudo="")
		sobre.save()
	return render(request, 'sobre.html', {'sobre': sobre })


@login_required
def sobre_editar(request):
	sobre = Sobre.objects.get(id=1)
	imagem = request.FILES.get('imagem', False)
	if request.method == 'POST' and imagem:
		fs = FileSystemStorage()
		filename = fs.save(imagem.name, imagem)
		uploaded_file_url = fs.url(filename)
		sobre.titulo = request.POST['titulo']
		sobre.conteudo = request.POST['conteudo']
		sobre.imagem = uploaded_file_url
		sobre.save()
		return redirect('sobre')
	elif request.method == 'POST' and sobre.imagem:
		sobre.titulo = request.POST['titulo']
		sobre.conteudo = request.POST['conteudo']
		sobre.save()
		return redirect('sobre')
	else: 	
		return render(request, 'sobre_editar.html', {'sobre': sobre })


@login_required
def email_enviar(request):
	request.POST['nome']
	request.POST['email']
	email = EmailMessage(request.POST['assunto'], request.POST['mensagem'], to=['irvaynematheus@hotmail.com'])
	email.send()
	return redirect('index')


@login_required
def cadeira_fundadores(request):
	try:
		cadeira_fundadores = CadeiraFundadoresTitulares.objects.all()
	except:
		cadeiras_fundadores = []
	return render(request, 'cadeira_fundadores.html', {'cadeira_fundadores': cadeira_fundadores})


@login_required
def cadeira_fundadores_cadastrar(request):
	if request.method == 'POST':
		imagem = request.FILES.get('imagem', False)
		in_memorian = request.POST.get('in_memorian', '') == 'on'
		if imagem:
			fs = FileSystemStorage()
			filename = fs.save(imagem.name, imagem)
			uploaded_file_url = fs.url(filename)
			cadeira_fundadores = CadeiraFundadoresTitulares(
				nome_fundador_titular=request.POST['nome_fundador_titular'],
				nome_membro_atual=request.POST['nome_membro_atual'],
				descricao_fundador_titular=request.POST['descricao_fundador_titular'],
				descricao_membro_atual=request.POST['descricao_membro_atual'],
				imagem_membro_atual=uploaded_file_url,
				in_memorian=in_memorian)
		else:
			cadeira_fundadores = CadeiraFundadoresTitulares(
				nome_fundador_titular=request.POST['nome_fundador_titular'],
				nome_membro_atual=request.POST['nome_membro_atual'],
				descricao_fundador_titular=request.POST['descricao_fundador_titular'],
				descricao_membro_atual=request.POST['descricao_membro_atual'],
				in_memorian=in_memorian)
		cadeira_fundadores.save()
		return redirect('cadeira_fundadores')
	else:
		return render(request, 'cadeira_fundadores_cadastrar.html')


@login_required
def cadeira_fundadores_editar(request, cadeira_fundadores_id):
	cadeira_fundadores = CadeiraFundadoresTitulares.objects.get(id=cadeira_fundadores_id)
	if request.method == 'POST':
		cadeira_fundadores.nome_fundador_titular = request.POST['nome_fundador_titular']
		cadeira_fundadores.nome_membro_atual = request.POST['nome_membro_atual']
		cadeira_fundadores.descricao_fundador_titular = request.POST['descricao_fundador_titular']
		cadeira_fundadores.descricao_membro_atual = request.POST['descricao_membro_atual']
		cadeira_fundadores.in_memorian = request.POST.get('in_memorian', '') == 'on'
		imagem = request.FILES.get('imagem', False)
		if imagem:
			fs = FileSystemStorage()
			filename = fs.save(imagem.name, imagem)
			uploaded_file_url = fs.url(filename)
			cadeira_fundadores.imagem_membro_atual=uploaded_file_url
		cadeira_fundadores.save()
		return redirect('cadeira_fundadores')
	else:
		return render(request, 'cadeira_fundadores_editar.html', {'cadeira_fundadores': cadeira_fundadores})


@login_required
def cadeira_fundadores_remover(request, cadeira_fundadores_id):
	cadeira_fundadores = CadeiraFundadoresTitulares.objects.get(id=cadeira_fundadores_id)
	cadeira_fundadores.delete()
	return redirect('cadeira_fundadores')