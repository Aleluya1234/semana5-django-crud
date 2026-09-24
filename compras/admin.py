from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cantidad", "comprado", "creado")
    list_filter = ("comprado", "creado")
    search_fields = ("nombre",)
