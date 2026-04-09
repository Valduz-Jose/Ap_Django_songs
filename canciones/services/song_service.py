from ..models import Cancion

class SongService:
    @staticmethod
    def obtener_todas():
        return Cancion.objects.all().order_by('-id')

    @staticmethod
    def crear_cancion(form_data):
        """Recibe el formulario validado y guarda en la BD"""
        return form_data.save()