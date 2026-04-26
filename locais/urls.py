from django.urls import path
from . import views

urlpatterns = [
    path('residuos/novo/', views.cadastrar_residuo, name='cadastrar_residuo'),
]