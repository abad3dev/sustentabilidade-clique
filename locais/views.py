from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LocalForm
from .models import Cidade
from django.contrib.auth.decorators import login_required

@login_required    
def cadastrar_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Local cadastrado com sucesso!')
            return redirect('cadastrar_local')
        else:
            messages.error(request, 'Erro ao cadastrar. Verifique os dados e tente novamente.')
    else:
        form = LocalForm()
  
    cidades = Cidade.objects.all().order_by('nome')
    
    return render(request, 'cadastrar_local.html', {'cidade': cidades})
        

def lista_locais_tipo(request):
    return render(request, 'lista_locais_tipo.html', {
        
    })

def lista_locais_bairro(request):
    return render(request, 'lista_locais_bairro.html', {
        
    })
