from django.db import models

class Torneio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Prova(models.Model):
    nome = models.CharField(max_length=100)
    torneio = models.ForeignKey(Torneio, on_delete=models.CASCADE, related_name='provas')

    def __str__(self):
        return self.nome

class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    torneios = models.ManyToManyField(Torneio, related_name='atletas')

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    atletas = models.ManyToManyField(Atleta, related_name='categorias')

    def __str__(self):
        return self.nome
