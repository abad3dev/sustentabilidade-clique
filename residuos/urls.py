from django.urls import path
from . import views

urlpatterns = [
    
    path('residuos/novo/', views.cadastrar_residuo, name='cadastrar_residuo'),
    path('residuos/consultar/', views.consultar_residuo, name='consultar_residuo'),
   
]