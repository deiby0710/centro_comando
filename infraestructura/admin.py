from django.contrib import admin
from .models import NodoServidor, RegistroAuditoria

def marcar_como_produccion(modeladmin, request, queryset):
    queryset.update(en_produccion=True)

def marcar_como_mantenimiento(modeladmin, request, queryset):
    queryset.update(en_produccion=False)

@admin.register(NodoServidor)
class NodoServidorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre_host',
        'direccion_ip',
        'motor_contenedores',
        'proxy_inverso',
        'en_produccion'
    )
    list_filter = (
        'motor_contenedores',
        'proxy_inverso',
        'en_produccion'
    )
    search_fields = ('nombre_host', 'direccion_ip')
    ordering = ('-fecha_despliegue',)
    actions = [
        marcar_como_produccion,
        marcar_como_mantenimiento
    ]

@admin.register(RegistroAuditoria)
class RegistroAuditoriaAdmin(admin.ModelAdmin):
    list_display = ('servidor', 'detalles', 'fecha_evento')
    list_filter = ('fecha_evento',)