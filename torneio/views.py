from django.shortcuts import render, redirect, get_object_or_404
from .models import Torneio, Atleta, Categoria
from .forms import TorneioForm

def torneios_view(request):
    torneios = Torneio.objects.all()
    return render(request, 'torneios.html', {'torneios': torneios})

def criar_torneio_view(request):
    form = TorneioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('torneios_view')
    return render(request, 'criar_torneio.html', {'form': form})

def editar_torneio_view(request, id):
    torneio = get_object_or_404(Torneio, id=id)
    form = TorneioForm(request.POST or None, instance=torneio)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('torneios_view')
    return render(request, 'editar_torneio.html', {'form': form})

def apagar_torneio_view(request, id):
    torneio = get_object_or_404(Torneio, id=id)
    if request.method == 'POST':
        torneio.delete()
        return redirect('torneios_view')
    return render(request, 'apagar_torneio.html', {'torneio': torneio})

def atleta_view(request, id):
    atleta = get_object_or_404(Atleta, id=id)
    return render(request, 'atleta.html', {'atleta': atleta})

def categorias_view(request):
    categorias = Categoria.objects.all().order_by('nome')
    return render(request, 'categorias.html', {'categorias': categorias})


