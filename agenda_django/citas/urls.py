from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agendar/', views.agendar_cita, name='agendar_cita'),
    path('consultar/', views.consultar_cita, name='consultar_cita'),
]
