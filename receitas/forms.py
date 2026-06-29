from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields=['nome','criador','ingredientes']
        labels={
            'nome':'Nome da Receita',
            'criador':'Criador da Receita',
            'ingredientes':'Ingredientes',
        }
        help_texts={
            'nome':'Ex: Cozido à Portuguesa',
        }