
from django.db import models

class  Tarefa(models.Model):
  id = models.AutoField(primary_key=True)
  titulo =  models.CharField(max_length= 200)
  inicio = models.DateField(verbose_name="Data de Início")
  entrega = models.DateField(verbose_name="Data de Entrega")
  descricao = models.CharField(max_length= 200, null=True)
  categoria = models.CharField(max_length=200)
  
  
  
  def __str__(self) -> str:
    return self.titulo