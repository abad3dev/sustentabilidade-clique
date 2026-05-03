from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ResiduoForm
from .models import Residuo

@login_required 
def cadastrar_residuo(request):
    if request.method == 'POST':
        form = ResiduoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resíduo cadastrado com sucesso!')
            return redirect('cadastrar_residuo')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')

    else:
        form = ResiduoForm()
    
    return render(request, 'cadastrar_residuo.html')

def consultar_residuo(request):
    
    residuos = Residuo.objects.all().order_by('nome')
    
    return render(request, 'consultar_residuo.html', {'residuos': residuos})
        
