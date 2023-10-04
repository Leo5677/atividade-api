from rest_framework import serializers
from .models import *

# SERIALIZADOR - ORDEM SERVIÇO
class OrdemServicoSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrdemServico
    fields = "__all__"
    
# SERIALIZADOR - EQUIPAMENTO
class EquipamentoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Equipamento
    fields = "__all__"