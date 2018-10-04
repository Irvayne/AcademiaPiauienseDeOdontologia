from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User

class RegistrarUsuarioView(View):

	template_name = 'registrar.html'

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		usuario = User.objects.create_user(request.POST['nome'], request.POST['email'], request.POST['senha'])
		return redirect('home')


		