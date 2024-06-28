from django.urls import path
from .views import visualizar_trabajadores, eliminar_documento, subir_documento

urlpatterns = [
    path('', visualizar_trabajadores, name='visualizar_trabajadores'),
    path('eliminar_documento/<int:documento_id>/', eliminar_documento, name='eliminar_documento'),
    path('subir_documento/<str:trabajador_rut>/', subir_documento, name='subir_documento'),
]
