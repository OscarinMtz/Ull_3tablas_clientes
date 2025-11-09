from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Clientes

def inicio_spa(request):
    return render(request, 'inicio.html')

def agregar_cliente(request):
    if request.method == 'POST':
        cliente = Clientes(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            email=request.POST['email'],
            telefono=request.POST['telefono'],
            alergias=request.POST.get('alergias', ''),
            preferencias=request.POST.get('preferencias', '')
        )
        cliente.save()
        messages.success(request, 'Cliente agregado correctamente!')
        return redirect('ver_clientes')
    return render(request, 'clientes/agregar_cliente.html')

def ver_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, id):
    try:
        cliente = Clientes.objects.get(id_clientes=id)
        if request.method == 'POST':
            cliente.nombre = request.POST['nombre']
            cliente.apellido = request.POST['apellido']
            cliente.email = request.POST['email']
            cliente.telefono = request.POST['telefono']
            cliente.alergias = request.POST.get('alergias', '')
            cliente.preferencias = request.POST.get('preferencias', '')
            cliente.save()
            messages.success(request, 'Cliente actualizado correctamente!')
            return redirect('ver_clientes')
        return render(request, 'clientes/actualizar_cliente.html', {'cliente': cliente})
    except Clientes.DoesNotExist:
        messages.error(request, 'El cliente no existe.')
        return redirect('ver_clientes')

def borrar_cliente(request, id):
    try:
        cliente = Clientes.objects.get(id_clientes=id)
        if request.method == 'POST':
            cliente.delete()
            messages.success(request, 'Cliente eliminado correctamente!')
            return redirect('ver_clientes')
        return render(request, 'clientes/borrar_cliente.html', {'cliente': cliente})
    except Clientes.DoesNotExist:
        messages.error(request, 'El cliente no existe.')
        return redirect('ver_clientes')