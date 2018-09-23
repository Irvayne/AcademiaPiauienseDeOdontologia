from django.db import models


class Estatuto(models.Model):
	conteudo = models.CharField(max_length=1000)


class Noticia(models.Model):
	titulo = models.CharField(max_length=1000)
	subtitulo = models.CharField(max_length=1000)
	conteudo = models.CharField(max_length=40000)
	criado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)
	imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)


class Diretoria(models.Model):
	nome = models.CharField(max_length=1000)
	descricao = models.CharField(max_length=1000)


class Membro(models.Model):
	nome = models.CharField(max_length=1000)
	descricao = models.CharField(max_length=1000)


class Curso(models.Model):
	nome = models.CharField(max_length=1000)
	descricao = models.CharField(max_length=1000)
	conteudo = models.CharField(max_length=1000)
	criado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)


class Cadeira(models.Model):
	nome = models.CharField(max_length=1000)
	descricao = models.CharField(max_length=1000)


class Sobre(models.Model):
	titulo = models.CharField(max_length=1000)
	conteudo = models.CharField(max_length=1000)


class Contato(models.Model):
	telefone = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	localizadao = models.CharField(max_length=100)