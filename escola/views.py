from django.shortcuts import render, get_object_or_404
from .models import Curso, Estudante

def cursos_view(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def estudante_view(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    return render(request, 'estudante.html', {'estudante': estudante})
