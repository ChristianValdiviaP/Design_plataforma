from django.urls import path
from .views import visualizar_informacion

urlpatterns = [
    path('visualizar/', visualizar_informacion, name='visualizar_informacion'),
]
