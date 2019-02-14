from django.db import models
from django.utils import timezone

class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)

    def __str__(self):
        return '%s, %s, %s, %s. %s - %s'% (self.logradouro, self.numero, self.complemento, self.bairro, self.cidade, self.estado)

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE) 
    telefone = models.CharField(max_length=18)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Pessoa: %s; endereço: %s'% (self.nome, self.endereco.logradouro)