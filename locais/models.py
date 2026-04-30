from django.db import models


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nome = models.TextField()
    sigla = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.nome} ({self.sigla})"

class Cidade(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    nome = models.TextField()
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, db_column='id_estado')
    def __str__(self):
        return f"{self.nome} - {self.id_estado.sigla}"

class Local(models.Model):
    id_local = models.AutoField(primary_key=True)
    nome = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    cep = models.TextField()
    logradouro = models.TextField()
    numero = models.IntegerField()
    complemento = models.TextField(blank=True, null=True)
    bairro = models.TextField()
    site = models.TextField(blank=True, null=True)
    horario = models.TextField()
    telefone = models.TextField()
    
    id_cidade = models.ForeignKey(
        Cidade, 
        on_delete=models.CASCADE, 
        db_column='id_cidade'
    )
    def __str__(self):
        return self.nome