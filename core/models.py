from django.db import models

class Estatuto(models.Model):

	conteudo = models.CharField(max_length=1000)
