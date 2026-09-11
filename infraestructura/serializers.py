from rest_framework import serializers

from .models import IncidenciaServidor, NodoServidor


class IncidenciaServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidenciaServidor
        fields = [
            'id',
            'servidor',
            'titulo',
            'descripcion',
            'severidad',
            'estado',
            'fecha_reporte',
        ]


class NodoServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodoServidor
        fields = [
            'id',
            'nombre_host',
            'direccion_ip',
            'motor_contenedores',
            'proxy_inverso',
            'en_produccion',
            'fecha_despliegue',
        ]