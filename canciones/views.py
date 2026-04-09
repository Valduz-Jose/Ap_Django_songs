from django.shortcuts import render, redirect
from .services.song_service import SongService
from .forms import CancionForm

def index(request):
    canciones = SongService.obtener_todas()
    return render(request, 'index.html', {'canciones': canciones})

def crear(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            SongService.crear_cancion(form)
            # .cleaned_data es un diccionario con los datos validados del formulario
            return redirect('index')
    else:
        form = CancionForm()
    
    return render(request, 'canciones_form.html', {'form': form, 'titulo_pagina': 'Agregar Canción'})