from django import forms
from .models import Candidato

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = [
            'nome',
            'endereco',
            'email',
            'telefone',
            'nascimento',
            'idade',
            'genero',
            'curriculo',
            'vaga',
        ]