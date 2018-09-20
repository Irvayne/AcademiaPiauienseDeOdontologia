from django.shortcuts import render
from core.models import Estatuto

def home(request):
	return render(request, 'home.html')

def estatuto(request):
	return render(request, 'estatuto.html', {'estatuto': Estatuto.objects.get(id=1) })

def estatuto_editar(request):
	if request.method == 'POST':
		
		estatuto = Estatuto.objects.get(id=1)
		estatuto.conteudo = request.POST['estatuto_conteudo']
		estatuto.save()
		return render(request, 'estatuto.html',  {'estatuto': Estatuto.objects.get(id=1)})
	else:
		estatuto = Estatuto.objects.get(id=1)
		#estatuto = Estatuto(conteudo='Digite o conteudo do estatuto')
		

	return render(request, 'estatuto_form.html', {'estatuto': estatuto })