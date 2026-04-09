from django.shortcuts import render
from .services.song_service import SongService

def index(request):
    # Capa de Servicio: obtenemos los datos
    canciones = SongService.obtener_todas()
    
    # Capa de Vista: enviamos los datos al template
    return render(request, 'index.html', {'canciones': canciones})