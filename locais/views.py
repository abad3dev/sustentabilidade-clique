from django.shortcuts import render, redirect
from .forms import ResiduoForm

def cadastrar_residuo(request):
    if request.method == 'POST':
        form = ResiduoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_residuo')
    else:
        form = ResiduoForm()
    
    return render(request, 'locais/html/cadastrar_residuo.html', {'form': form})
