from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_productos, name="lista_productos"),
    path("borrar/<int:id>/", views.borrar_producto, name="borrar_producto"),
]
