from django.shortcuts import render, redirect, get_object_or_404
from .models import Veterinario, Animal, Consulta, Especialidade
from .forms import ConsultaForm, AnimalForm

def consultas_view(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas.html', {'consultas': consultas})

def criar_consulta_view(request):
    form = ConsultaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('consultas_view')
    return render(request, 'criar_consulta.html', {'form': form})

def editar_consulta_view(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    form = ConsultaForm(request.POST or None, instance=consulta)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('consultas_view')
    return render(request, 'editar_consulta.html', {'form': form})

def apagar_consulta_view(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consultas_view')
    return render(request, 'apagar_consulta.html', {'consulta': consulta})

def veterinario_view(request, id):
    veterinario = get_object_or_404(Veterinario, id=id)
    return render(request, 'veterinario.html', {'veterinario': veterinario})

def especialidades_view(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'especialidades.html', {'especialidades': especialidades})

def animais_view(request):
    animais = Animal.objects.all()
    return render(request, 'animais.html', {'animais': animais})

def criar_animal_view(request):
    form = AnimalForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('animais_view')
    return render(request, 'animais.html', {'form': form})

def editar_animal_view(request, id):
    animal = get_object_or_404(Animal, id=id)
    form = AnimalForm(request.POST or None, instance=animal)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('animais_view')
    return render(request, 'editar_animal.html', {'form': form})

def apagar_animal_view(request, id):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        animal.delete()
        return redirect('animais_view')
    return render(request, 'apagar_animal_view', {'animal': animal})
