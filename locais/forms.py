from django import forms
from .models import Residuo

class ResiduoForm(forms.ModelForm):
    class Meta:
        model = Residuo
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exemplo: Papel, Vidro...'})
        }