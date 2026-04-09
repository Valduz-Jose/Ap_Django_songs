from django.shortcuts import get_object_or_404
from ..models import Cancion

class SongService:
    @staticmethod
    def obtener_todas():
        return Cancion.objects.all().order_by('-id')

    @staticmethod
    def obtener_por_id(id):
        """Busca una canción o lanza un error 404 si no existe"""
        return get_object_or_404(Cancion, id=id)

    @staticmethod
    def crear_o_actualizar(form_data):
        """Guarda tanto creaciones como ediciones"""
        return form_data.save()

    @staticmethod
    def eliminar_cancion(cancion):
        """Elimina el registro de la base de datos"""
        cancion.delete()