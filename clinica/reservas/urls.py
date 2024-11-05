from django.urls import path
from . import views

urlpatterns = [
    path('reservar/', views.reservar_cita, name='reservar_cita'),
    path('citas/', views.listar_citas, name='citas'),
]
