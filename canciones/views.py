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
            # CAMBIA SongService.crear_cancion(form) POR:
            SongService.crear_o_actualizar(form) 
            return redirect('index')
    else:
        form = CancionForm()
    
    return render(request, 'canciones_form.html', {
        'form': form, 
        'titulo_pagina': 'Nueva Canción'
    })

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

def eliminar(request, id):
    cancion = SongService.obtener_por_id(id)
    
    if request.method == 'POST':
        SongService.eliminar_cancion(cancion)
        return redirect('index')
        
    return render(request, 'canciones_confirm_delete.html', {'cancion': cancion})