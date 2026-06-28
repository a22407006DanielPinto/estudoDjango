from django.shortcuts import render, get_object_or_404
from .models import Torneio, Atleta

def torneios_view(request):
    torneios = Torneio.objects.all()
    return render(request, 'torneios.html', {'torneios': torneios})

def atleta_view(request, id):
    atleta = get_object_or_404(Atleta, id=id)
    return render(request, 'atleta.html', {'atleta': atleta})


