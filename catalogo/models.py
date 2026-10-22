from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    activa = models.BooleanField(default=True, verbose_name="¿Está Activa?")
    creada_el = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        ordering = ['nombre']
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    # RELACIÓN 1: Categoría a Producto (Un producto pertenece a una categoría)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT, # PROTECT evita borrar una categoría si tiene productos asociados
        related_name='productos', # Permite hacer: categoria.productos.all()
        verbose_name="Categoría"
    )
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción Corta")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio ($)")
    stock = models.IntegerField(default=0, verbose_name="Cantidad en Stock")
    imagen_principal = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Foto Principal")
    destacado = models.BooleanField(default=False, verbose_name="¿Producto Destacado?")
    actualizado_el = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        ordering = ['-actualizado_el'] # Los más nuevos editados aparecen primero
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class ImagenAdicional(models.Model):
    # RELACIÓN 2: Producto a ImagenAdicional (Un producto puede tener muchas fotos extras)
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, # Si se borra el producto, se borran automáticamente sus fotos extras
        related_name='imagenes_extras', # Permite hacer: producto.imagenes_extras.all()
        verbose_name="Producto"
    )
    imagen = models.ImageField(upload_to='productos/galeria/', verbose_name="Foto Adicional")
    orden = models.PositiveIntegerField(default=0, verbose_name="Orden de Visualización")

    class Meta:
        ordering = ['orden']
        verbose_name = "Imagen Adicional"
        verbose_name_plural = "Imágenes Adicionales"

    def __str__(self):
        return f"Foto extra de {self.producto.nombre} (Posición {self.orden})"
    