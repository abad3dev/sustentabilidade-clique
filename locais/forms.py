from django import forms
from .models import Residuo, Local

class ResiduoForm(forms.ModelForm):
    class Meta:
        model = Residuo
        fields = ['nome']
class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nome', 'cep', 'id_cidade', 'logradouro', 'numero', 'complemento', 'bairro', 'latitude', 'longitude', 'telefone', 'site', 'horario']