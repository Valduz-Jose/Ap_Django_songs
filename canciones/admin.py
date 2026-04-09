from django.contrib import admin
from .models import Cancion

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'artista', 'popularidad') # Columnas visibles en la lista
    search_fields = ('titulo', 'artista')               # Barra de búsqueda
    list_filter = ('popularidad',)                     # Filtro lateral