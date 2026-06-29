from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Estudante
from .forms import CursoForm

def cursos_view(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def criar_curso_view(request):
    form = CursoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cursos_view')
    return render(request, 'criar_curso.html', {'form': form})

def editar_curso_view(request, id):
    curso = get_object_or_404(Curso, id=id)
    form = CursoForm(request.POST or None, instance=curso)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cursos_view')
    return render(request, 'editar_curso.html', {'form': form})

def apagar_curso_view(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos_view')
    return render(request, 'apagar_curso.html', {'curso': curso})

def estudante_view(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    return render(request, 'estudante.html', {'estudante': estudante})
