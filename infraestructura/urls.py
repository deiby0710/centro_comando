from django.urls import path
from .views import ApiRootView, IncidenciaServidorDetailAPIView, IncidenciaServidorListCreateAPIView, NodoServidorDetailAPIView, NodoServidorListCreateAPIView, crear_incidencia, crear_servidor, editar_servidor, eliminar_servidor, lista_servidores, detalle_servidor, resolver_incidencia

urlpatterns = [
    path('', lista_servidores, name='home_servidores'),
    path('servidor/<int:pk>', detalle_servidor, name='detalle_servidor'),
    path('servidor/nuevo/', crear_servidor, name='crear_servidor'),
    path('servidor/<int:pk>/editar/', editar_servidor, name='editar_servidor'),
    path('servidor/<int:pk>/eliminar/', eliminar_servidor, name='eliminar_servidor'),
    path('servidor/<int:pk>/incidencia/nueva/', crear_incidencia, name='crear_incidencia'),
    path('incidencia/<int:pk>/resolver/', resolver_incidencia, name='resolver_incidencia'),
    path('api/incidencias/', IncidenciaServidorListCreateAPIView.as_view(), name='api_incidencias'),
    path('api/incidencias/', IncidenciaServidorListCreateAPIView.as_view(),name='api_incidencias'),
    path('api/incidencias/<int:pk>/', IncidenciaServidorDetailAPIView.as_view(),name='api_incidencia_detalle'),
    path('api/servidores/', NodoServidorListCreateAPIView.as_view(),name='api_servidores'),
    path('api/servidores/<int:pk>/',NodoServidorDetailAPIView.as_view(),name='api_servidor_detalle'),
    path('api/', ApiRootView.as_view(), name='api-root'),
]