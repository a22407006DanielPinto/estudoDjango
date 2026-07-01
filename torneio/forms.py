from django import forms
from .models import Torneio, Prova

class TorneioForm(forms.ModelForm):
    class Meta:
        model = Torneio
        fields=['nome','descricao']
        labels={
            'nome':'Nome do Torneio',
            'descricao':'Descrição do Torneio'
        }
        text_helps={
            'nome':'Ex: Campeonato Nacional'
        }

class ProvaForm(forms.ModelForm):
    class Meta:
        model = Prova
        fields=['nome']
        labels={
            'nome':'Nome da Prova',
        }
        text_helps={
            'nome':'Ex: Triplo Salto'
        }
