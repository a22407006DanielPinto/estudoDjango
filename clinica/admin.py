from django.contrib import admin
from .models import Veterinario, Animal, Consulta, Especialidade

admin.site.register(Veterinario)
admin.site.register(Animal)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display=['data','motivo','veterinario','animal']
    fields=['data','motivo','veterinario','animal']
    search_fields=['veterinario__nome']

@admin.register(Especialidade)
class EspecialidadeAdmin(admin.ModelAdmin):
    filter_horizontal=['veterinarios']