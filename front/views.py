from django.shortcuts import render
from core.models import Estatuto

def index(request):
	return render(request, 'index.html')

def estatuto(request):
	estatuto = Estatuto.objects.get(id=1)
	return render(request, 'front_estatuto.html', {'estatuto': estatuto })