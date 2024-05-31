from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ingresar_trabajador'),
    path('eliminar_documento/<int:id>/', views.eliminar_documento, name='eliminar_documento'),
]

