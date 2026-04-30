from django import forms
from .models import Local

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'cep', 'id_cidade', 'logradouro', 'numero', 'complemento', 'bairro', 'latitude', 'longitude', 'telefone', 'site', 'horario']