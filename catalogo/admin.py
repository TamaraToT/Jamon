from django.contrib import admin
from .models import Categoria, Producto, ImagenAdicional

# 1. Configuración de la cabecera y título del panel en español
admin.site.site_header = "Panel de Administración de Mi Negocio"
admin.site.site_title = "Mi Negocio Admin"
admin.site.index_title = "Bienvenido al Gestor del Negocio"

# 2. Inline para gestionar los hijos (Imágenes) desde el padre (Producto)
class ImagenAdicionalInline(admin.TabularInline):
    model = ImagenAdicional
    extra = 1  # Número de formularios vacíos que aparecen por defecto
    fields = ['imagen', 'orden']

# 3. Inline para gestionar los hijos (Productos) desde el padre (Categoría)
class ProductoInline(admin.TabularInline):
    model = Producto
    extra = 1
    fields = ['nombre', 'precio', 'stock', 'destacado']

# 4. Registro y configuración del modelo Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activa', 'creada_el')
    list_filter = ('activa', 'creada_el')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)
    inlines = [ProductoInline]  # Permite crear productos directamente desde la categoría

# 5. Registro y configuración del modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'destacado', 'actualizado_el')
    list_filter = ('categoria', 'destacado', 'actualizado_el')
    search_fields = ('nombre', 'descripcion', 'categoria__nombre')
    ordering = ('-actualizado_el',)
    inlines = [ImagenAdicionalInline]  # Permite subir fotos extras directamente desde el producto
