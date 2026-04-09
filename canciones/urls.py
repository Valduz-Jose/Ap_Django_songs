from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear, name='canciones_crear'),
    path('editar/<int:id>/', views.editar, name='canciones_editar'), 
]