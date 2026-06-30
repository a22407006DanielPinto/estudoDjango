from django.shortcuts import render, redirect, get_object_or_404
from .models import Veterinario, Animal, Consulta

def consultas_view(request):
    consultas = Consulta.object.all()
    return render(request, 'consultas.html', {'consultas': consultas})

def veterinario_view(request, id):
    veterinario = get_object_or_404(Veterinario, id=id)
    return render(request, 'veterinario.html', {'veterinario': veterinario})
