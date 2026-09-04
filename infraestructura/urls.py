from django.urls import path
from .views import crear_servidor, editar_servidor, eliminar_servidor, lista_servidores, detalle_servidor

urlpatterns = [
    path('', lista_servidores, name='home_servidores'),
    path('servidor/<int:pk>', detalle_servidor, name='detalle_servidor'),
    path('servidor/nuevo/', crear_servidor, name='crear_servidor'),
    path('servidor/<int:pk>/editar/', editar_servidor, name='editar_servidor'),
    path('servidor/<int:pk>/eliminar/', eliminar_servidor, name='eliminar_servidor'),
]