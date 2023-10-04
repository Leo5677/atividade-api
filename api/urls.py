from django.urls import path
from . import views

# URLS
urlpatterns = [
  # URL - CRIA E/OU OBTÉM TODAS AS ORDENS DE SERVIÇO
  path(
    'v1/os/',
    views.OrdemServicoViewGetPost.as_view(),
    name='os-obter-todas'
  ),
  
  # URL - OBTÉM A ORDEM DE SERVIÇO COM BASE NO CAMPO NÚMERO
  path(
    'v1/os/<str:numero>/',
    views.OrdemServicoViewGetByNumero.as_view(),
    name='os-obter-por-numero'
  ),
  
  # URL - OBTÉM TODOS OS EQUIPAMENTOS DE UMA ORDEM DE SERVIÇO
  path(
    'v1/os/<str:numero>/equipamento/',
    views.EquipamentoByNumeroOs.as_view(),
    name='equipamento-obter-por-numero-os'
  ),
  
  # URL - OBTÉM TODOS OS EQUIPAMENTOS DE UMA ORDEM DE SERVIÇO E COM UM ÍNDICE
  path(
    'v1/os/<str:numero>/equipamento/<int:indice>/',
    views.EquipamentoByNumeroOsIndice.as_view(),
    name='equipamento-obter-por-numero-os-indice'
  ),
  
  # URL - OBTÉM TODOS OS EQUIPAMENTOS COM UMA DETERMINADA DESCRIÇÃO
  path(
    'v1/os/equipamento/<str:descricao>/',
    views.EquipamentoByDescricao.as_view(),
    name='equipamento-obter-por-descricao'
  ),
]
