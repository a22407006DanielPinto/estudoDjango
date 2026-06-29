from django import forms
from .models import Consulta

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