# semana5-django-crud
## Circuito formulario → lista

1. El usuario escribe el nombre y la cantidad en el formulario y presiona "Agregar".
2. El navegador envía esos datos por POST a la URL raíz (`/`).
3. La vista `lista_productos` recibe el POST, lee `nombre` y `cantidad` de `request.POST`, y usa `Producto.objects.create()` para guardarlos en la base de datos vía el ORM.
4. Tras guardar, la vista redirige (patrón POST-redirect-GET) a la misma URL, ahora como GET.
5. En el GET, la vista consulta `Producto.objects.all().order_by("-creado")` y pasa esa lista al template, que la recorre con `{% for %}` y la muestra en pantalla.
