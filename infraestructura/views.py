from django.shortcuts import get_object_or_404, render
from .models import NodoServidor

def detalle_servidor(request, pk):
	nodo = get_object_or_404(NodoServidor, pk=pk)
	return render(request, 'infraestructura/detalle.html', {'nodo':nodo})

def lista_servidores(request):
	servidores = NodoServidor.objects.all()
	contexto = {'servidores': servidores}
	return render(request, 'infraestructura/index.html', contexto)