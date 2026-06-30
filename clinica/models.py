from django.db import models

class Veterinario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    dono = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    data = models.DateField()
    motivo = models.CharField(max_length=100)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='consultas')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='consultas_animais')

    def __str__(self):
        return f"{self.animal} - {self.data}"

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    veterinarios = models.ManyToManyField(Veterinario, related_name='especialidades')

    def __str__(self):
        return self.nome
