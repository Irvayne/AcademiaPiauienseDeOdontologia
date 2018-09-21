from django.db import models

class Estatuto(models.Model):

	conteudo = models.CharField(max_length=1000)


class Noticia(models.Model):

	titulo = models.CharField(max_length=1000)
	subtitulo = models.CharField(max_length=1000)
	conteudo = models.CharField(max_length=40000)

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

class Cadeira(models.Model):

	nome = models.CharField(max_length=1000)
	descricao = models.CharField(max_length=1000)

class Sobre(models.Model):

	conteudo = models.CharField(max_length=1000)
	
		