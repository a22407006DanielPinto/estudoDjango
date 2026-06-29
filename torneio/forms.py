from django import forms
from .models import Torneio

class TorneioForm(forms.ModelForm):
    class Meta:
        model = Torneio
        fields=['nome']
        labels={
            'nome':'Nome do Torneio',
        }
        text_helps={
            'nome':'Ex: Campeonato Nacional'
        }