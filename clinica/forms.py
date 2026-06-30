from django import forms
from .models import Consulta, Animal

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields=['data','motivo','veterinario','animal']
        labels={
            'data':'Data da Consulta',
            'motivo':'Motivo da Consulta',
            'veterinario':'Nome do Veterinário',
            'animal':'Nome do Animal',
        }
        help_texts={
            'data':'Ex: 26/07/2026',
        }

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields=['nome','especie','dono']
        labels={
            'nome':'Nome do Animal',
            'especie':'Espécie do Animal',
            'dono':'Nome do Dono',
        }
        help_texts={
            'especie':'Ex: Gato',
        }