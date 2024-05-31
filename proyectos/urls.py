from django.urls import path
from .views import proyectos_index, eliminar_info

urlpatterns = [
    path('', proyectos_index, name='proyectos_index'),
    path('eliminar_info/<int:index>/', eliminar_info, name='eliminar_info'),
]

