from django.shortcuts import render, redirect
from .forms import ResiduoForm, LocalForm
from .models import Cidade

def index(request):
    return render(request, 'inicial.html')

    
def cadastrar_residuo(request):
    if request.method == 'POST':
        form = ResiduoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_residuo')
    else:
        form = ResiduoForm()
    
    return render(request, 'cadastrar_residuo.html')

def cadastrar_local(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_local')

    else:
        form = LocalForm()
  
    cidades = Cidade.objects.all().order_by('nome')
    
    return render(request, 'cadastrar_local.html', {'cidade': cidades})
        

def lista_locais_tipo(request):
    return render(request, 'lista_locais_tipo.html', {
        
    })

def lista_locais_cep(request):
    return render(request, 'lista_locais_cep.html', {
        
    })
