import uuid
from django.db import models

# MODEL - ORDEM SERVIÇO
class OrdemServico(models.Model):
  id_os = models.AutoField(primary_key=True)
  numero = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
  descricao = models.TextField(max_length=255)
  
  def __str__(self):
    return "Ordem Serviço - " + str(self.numero)
  
# MODEL - EQUIPAMENTO
class Equipamento(models.Model):
  id_equipamento = models.AutoField(primary_key=True)
  numero = models.ForeignKey(
    OrdemServico,
    to_field="numero",
    on_delete=models.DO_NOTHING
  )
  indice = models.IntegerField()
  descricao = models.CharField(max_length=150)
  problema = models.TextField(max_length=255)
  
  def __str__(self):
    return "Equipamento - " + str(self.id_equipamento)
