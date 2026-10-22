from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

# 1. Portada que lista los productos usando el ORM
def portada(request):
    # Traemos solo los productos destacados o todos los activos
    productos = Producto.objects.all()
    categorias = Categoria.objects.filter(activa=True)
    
    return render(request, 'portada.html', {
        'productos': productos,
        'categorias': categorias
    })

# 2. Página de detalle (Si el ID no existe, lanza un 404 limpio)
def detalle_producto(request, producto_id):
    # get_object_or_404 evita el error 500 si inventan un ID en la URL
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'detalle.html', {'producto': producto})
