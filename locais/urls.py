from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('residuos/novo/', views.cadastrar_residuo, name='cadastrar_residuo'),
    path('locais/novo/', views.cadastrar_local, name='cadastrar_local'),
    path('locais/cep/', views.lista_locais_cep, name='lista_locais_cep'),
    path('locais/tipo/', views.lista_locais_tipo, name='lista_locais_tipo'),
    
]