from django.shortcuts import render, redirect
from core.models import Estatuto, Noticia

def home(request):
	return render(request, 'home.html')

def estatuto(request):
	return render(request, 'estatuto.html', {'estatuto': Estatuto.objects.get(id=1) })

def estatuto_form(request):
	if request.method == 'POST':
		
		estatuto = Estatuto.objects.get(id=1)
		estatuto.conteudo = request.POST['estatuto_conteudo']
		estatuto.save()
		return render(request, 'estatuto.html',  {'estatuto': Estatuto.objects.get(id=1)})
	else:
		estatuto = Estatuto.objects.get(id=1)
		#estatuto = Estatuto(conteudo='Digite o conteudo do estatuto')
		

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