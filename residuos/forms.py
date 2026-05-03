from django import forms
from .models import Residuo

class ResiduoForm(forms.ModelForm):
    class Meta:
        model = Residuo
        fields = ['nome','info']
