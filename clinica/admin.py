from django.contrib import admin
from .models import Veterinario, Animal, Consulta, Especialidade

admin.site.register(Veterinario)
admin.site.register(Animal)
admin.site.register(Consulta)
admin.site.register(Especialidade)