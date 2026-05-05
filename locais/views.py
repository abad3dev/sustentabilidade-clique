from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LocalForm
from .models import Cidade, Local
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

def consultar_locais_bairro(request):
   
    locais_bairro = []

    if request.method == 'POST':
        
        termo = request.POST.get('bairro', '').strip()
        
        if termo:
            
            locais_bairro = Local.objects.filter(bairro__icontains=termo).order_by('nome')
        else:
            
            locais_bairro = Local.objects.all().order_by('nome')

    return render(request, 'consultar_locais_bairro.html', {'locais_bairro': locais_bairro})
     
    

def consultar_locais(request):
    
    locais = Local.objects.all().order_by('nome')
    
    return render(request, 'consultar_locais.html', {'locais': locais})