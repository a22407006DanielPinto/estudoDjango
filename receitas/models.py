from django.db import models

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Receita(models.Model):
    nome = models.CharField(max_length=100)
    criador = models.ForeignKey(Utilizador, on_delete=models.CASCADE, related_name='receitas_criadas')
    ingredientes = models.ManyToManyField(Ingrediente, related_name='receitas')
    favoritos = models.ManyToManyField(Utilizador, related_name='receitas_favoritas')

    def __str__(self):
        return self.nome