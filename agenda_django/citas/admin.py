from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'fecha', 'hora', 'activa')
    list_filter = ('activa', 'fecha')
    search_fields = ('codigo', 'nombre', 'telefono')
