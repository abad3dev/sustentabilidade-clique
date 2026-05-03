from django.urls import path
from . import views

urlpatterns = [
    
    path('locais/novo/', views.cadastrar_local, name='cadastrar_local'),
    path('locais/consultar/', views.consultar_locais, name='consultar_locais'),
    path('locais/bairro/', views.lista_locais_bairro, name='lista_locais_bairro'),
    path('locais/tipo/', views.lista_locais_tipo, name='lista_locais_tipo'),
    
]
