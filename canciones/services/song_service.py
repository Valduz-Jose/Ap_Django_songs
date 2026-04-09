from ..models import Cancion

class SongService:
    @staticmethod
    def obtener_todas():
        """Retorna todas las canciones ordenadas por ID ascendente"""
        return Cancion.objects.all().order_by('id')