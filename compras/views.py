from django.shortcuts import render, redirect
from .models import Producto


def lista_productos(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        cantidad = request.POST.get("cantidad")
        if nombre and cantidad:
            Producto.objects.create(nombre=nombre, cantidad=cantidad)
        return redirect("lista_productos")

    productos = Producto.objects.all().order_by("-creado")
    return render(request, "compras/lista.html", {"productos": productos})


def borrar_producto(request, id):
    Producto.objects.get(id=id).delete()
    return redirect("lista_productos")
