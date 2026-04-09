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

def editar(request, id):
    cancion = SongService.obtener_por_id(id)
    
    if request.method == 'POST':
        # Pasamos instance=cancion para que Django sepa que estamos EDITANDO, no creando
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            SongService.crear_o_actualizar(form)
            return redirect('index')
    else:
        form = CancionForm(instance=cancion)
    
    return render(request, 'canciones_form.html', {
        'form': form, 
        'titulo_pagina': 'Editar Canción'
    })