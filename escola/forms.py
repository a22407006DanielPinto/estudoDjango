from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields=['nome','professor']
        labels={
            'nome': 'Nome do Curso',
            'professor': 'Professor responsável'
        }
        help_texts={
            'nome': 'Ex: Inglês A1'
        }