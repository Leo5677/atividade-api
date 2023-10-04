from django.contrib import admin
from .models import OrdemServico, Equipamento

# ADMIN - ORDEM SERVIÇO
class OrdemServicoAdmin(admin.ModelAdmin):
  list_display = ("id_os", "numero", "descricao")
  readonly_fields = ("numero",)
  
#ADMIN - EQUIPAMENTOS
class EquipamentoAdmin(admin.ModelAdmin):
  list_display = ("id_equipamento", "numero", "indice", "descricao", "problema")
  
admin.site.register(OrdemServico, OrdemServicoAdmin)
admin.site.register(Equipamento, EquipamentoAdmin)
