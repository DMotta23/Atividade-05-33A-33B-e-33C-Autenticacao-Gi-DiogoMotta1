from django.db import models


class PratosMassa(models.Model):
    nivel_de_dificuldade = [("F", "Facil"), ("M", "Medio"), ("D", "Dificil")]

    nome = models.CharField(max_length=40)
    tipoMassa = models.CharField(max_length=20)
    dificuldade = models.CharField(max_length=10, choices=nivel_de_dificuldade)
    numCalorias = models.IntegerField()


class Utensilios(models.Model):
    tipos_de_tamanho = [("P", "Pequeno"), ("M", "Medio"), ("G", "Grande")]

    nome = models.CharField(max_length=20)
    material = models.CharField(max_length=8)
    cortante = models.BooleanField()
    tamanho = models.CharField(max_length=1, choices=tipos_de_tamanho)


class Porcoes(models.Model):
    nome = models.CharField(max_length=20)
    quantidade = models.IntegerField()
