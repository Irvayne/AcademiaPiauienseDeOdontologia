from django.db import models

class Estatuto(models.Model):

	conteudo = models.CharField(max_length=1000)


class Noticia(models.Model):

	titulo = models.CharField(max_length=1000)
	subtitulo = models.CharField(max_length=1000)
	conteudo = models.CharField(max_length=40000)