from django.db import models
from locais.models import Local

class Residuo(models.Model):
    id_residuo = models.AutoField(primary_key=True)
    nome = models.TextField()
    info = models.TextField()
    def __str__(self):
        return self.nome


class Residuo_Local(models.Model):
    
    id_local = models.ForeignKey(
        Local, 
        on_delete=models.CASCADE, 
        db_column='id_local'
    )
    
    
    id_residuo = models.ForeignKey(
        Residuo, 
        on_delete=models.CASCADE, 
        db_column='id_residuo'
    )
    def __str__(self):
        return f"{self.id_local.nome} - {self.id_residuo.nome}"# Create your models here.
