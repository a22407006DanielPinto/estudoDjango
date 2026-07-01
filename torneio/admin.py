from django.contrib import admin
from .models import Torneio, Prova, Atleta, Categoria

admin.site.register(Torneio)
admin.site.register(Prova)
admin.site.register(Atleta)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=['nome']
    filter_horizontal=['atletas']
