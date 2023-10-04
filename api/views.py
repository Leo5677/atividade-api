from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import permissions
from django_filters.rest_framework import *

# VIEW - ORDEM SERVIÇO - GET E POST
class OrdemServicoViewGetPost(generics.ListCreateAPIView):
  queryset = OrdemServico.objects.all()
  serializer_class = OrdemServicoSerializer
  filterset_fields = ['id_os', 'numero', 'descricao'] 
  
# VIEW - ORDEM SERVIÇO - GET BY NÚMERO
class OrdemServicoViewGetByNumero(generics.ListAPIView):
  queryset = OrdemServico.objects.all()
  serializer_class = OrdemServicoSerializer
  lookup_field = 'numero'
  filterset_fields = ['id_os', 'numero', 'descricao']
  
  # RETORNA A ORDEM DE SERVIÇO COM O NÚMERO PESQUISADO
  def get_queryset(self):
    numero = self.kwargs['numero']
    return OrdemServico.objects.filter(numero=numero)

# VIEW - EQUIPMAENTO - GET BY NÚMERO DE ORDEM DE SERVIÇO
class EquipamentoByNumeroOs(generics.ListCreateAPIView):
  serializer_class = EquipamentoSerializer
  lookup_field = 'numero'
  filterset_fields = ['id_equipamento', 'indice', 'descricao', 'problema', 'numero'] 
  
  def get_queryset(self):
    numero = self.kwargs['numero']
    return Equipamento.objects.filter(numero__numero=numero)
  
# VIEW - EQUIPAMENTO - GET BY NÚMERO DE ORDEM DE SERVIÇO E ÍNDICE
class EquipamentoByNumeroOsIndice(generics.ListAPIView):
  serializer_class = EquipamentoSerializer
  filterset_fields = ['id_equipamento', 'indice', 'descricao', 'problema', 'numero'] 
  
  def get_queryset(self):
    numero = self.kwargs['numero']
    indice = self.kwargs['indice']
    
    return Equipamento.objects.filter(numero__numero=numero, indice=indice)
    
  
# VIEW - EQUIPAMENTO GET BY DESCRIÇÃO
class EquipamentoByDescricao(generics.ListAPIView):
  serializer_class = EquipamentoSerializer
  lookup_field = 'descricao'
  filterset_fields = ['id_equipamento', 'indice', 'descricao', 'problema', 'numero'] 
  
  def get_queryset(self):
    descricao = self.kwargs['descricao']
    return Equipamento.objects.filter(descricao=descricao)
  