from django.contrib import admin
from .models import Veterinario, Animal, Consulta

admin.site.register(Veterinario)
admin.site.register(Animal)
admin.site.register(Consulta)