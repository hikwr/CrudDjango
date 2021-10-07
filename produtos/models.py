from django.db import models
from django.contrib.auth.models import User


class Posicao(models.Model):
    titulo = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.titulo

class Usuario (models.Model):
    usuarios = models.ManyToManyField(User)
    


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()
    criado = models.DateField(auto_now_add = True)
    posicao = models.ForeignKey(Posicao, on_delete = models.CASCADE, default= None )
    usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao







