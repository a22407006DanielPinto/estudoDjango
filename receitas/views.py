from django.shortcuts import render, get_object_or_404
from .models import Receita, Utilizador

def receitas_view(request):
    receitas = Receita.objects.all()
    return render(request, 'receitas.html', {'receitas': receitas})

def utilizador_view(request, id):
    utilizador = get_object_or_404(Utilizador, id=id)
    return render(request, 'utilizador.html', {'utilizador': utilizador})




