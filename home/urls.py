from django.urls import path
from .views import seleccionar_accion

urlpatterns = [
    path('', seleccionar_accion, name='seleccionar_accion'),
]
