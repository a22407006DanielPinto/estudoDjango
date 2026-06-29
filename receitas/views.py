from django.shortcuts import render, redirect, get_object_or_404
from .models import Receita, Utilizador
from .forms import ReceitaForm

def receitas_view(request):
    receitas = Receita.objects.all()
    return render(request, 'receitas.html', {'receitas': receitas})

def criar_receita_view(request):
    form = ReceitaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('receitas_view')
    return render(request, 'criar_receita.html', {'form': form})

def editar_receita_view(request, id):
    receita = get_object_or_404(Receita, id=id)
    form = ReceitaForm(request.POST or None, instance=receita)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('receitas_view')
    return render(request, 'editar_receita.html', {'form': form})

def apagar_receita_view(request, id):
    receita = get_object_or_404(Receita, id=id)
    if request.method == 'POST':
        receita.delete()
        return redirect('receitas_view')
    return render(request, 'apagar_receita.html', {'receita': receita})

def utilizador_view(request, id):
    utilizador = get_object_or_404(Utilizador, id=id)
    return render(request, 'utilizador.html', {'utilizador': utilizador})




