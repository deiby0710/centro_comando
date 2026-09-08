from django.shortcuts import get_object_or_404, redirect, render
from infraestructura.forms import IncidenciaServidorForm, NodoServidorForm
from .models import IncidenciaServidor, NodoServidor

def eliminar_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        nodo.delete()
        return redirect('home_servidores')
    return render(request, 'infraestructura/eliminar_servidor.html', {'nodo': nodo})

def editar_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        form = NodoServidorForm(request.POST, instance=nodo)
        if form.is_valid():
            form.save()
            return redirect('detalle_servidor', pk=nodo.pk)
    else:
        form = NodoServidorForm(instance=nodo)
    return render(request, 'infraestructura/editar_servidor.html', {'form': form, 'nodo': nodo})

def crear_servidor(request):
    if request.method == 'POST':
        form = NodoServidorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_servidores')
    else:
        form = NodoServidorForm()
    return render(request, 'infraestructura/crear_servidor.html', {'form': form})


def detalle_servidor(request, pk):
    nodo = get_object_or_404(NodoServidor, pk=pk)
    incidencias_activas = nodo.incidencias.exclude(estado='RESUELTA')
    return render(
        request,
        'infraestructura/detalle.html',
        {
            'nodo': nodo,
            'incidencias_activas': incidencias_activas,
        }
    )

def lista_servidores(request):
	servidores = NodoServidor.objects.all()
	contexto = {'servidores': servidores}
	return render(request, 'infraestructura/index.html', contexto)

def crear_incidencia(request, pk):
    servidor = get_object_or_404(NodoServidor, pk=pk)
    if request.method == 'POST':
        form = IncidenciaServidorForm(request.POST)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.servidor = servidor
            incidencia.save()
            return redirect('detalle_servidor', pk=servidor.pk)
    else:
        form = IncidenciaServidorForm()
    return render(
        request,
        'infraestructura/crear_incidencia.html',
        {
            'form': form,
            'servidor': servidor,
        }
    )

def resolver_incidencia(request, pk):
    incidencia = get_object_or_404(IncidenciaServidor, pk=pk)
    if request.method == 'POST':
        incidencia.estado = 'RESUELTA'
        incidencia.save()
        return redirect('detalle_servidor', pk=incidencia.servidor.pk)
    return redirect('detalle_servidor', pk=incidencia.servidor.pk)