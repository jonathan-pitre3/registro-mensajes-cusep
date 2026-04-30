from django.contrib import admin
from .models import SolicitudServicio


@admin.register(SolicitudServicio)
class SolicitudServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre_receptor', 'tipo_servicio', 'status', 'fecha_solicitud')
    list_filter = ('status', 'tipo_servicio')
