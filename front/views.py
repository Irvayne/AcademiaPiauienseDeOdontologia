from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Bem-Vindo à Academia Piauiense de Odontologia')