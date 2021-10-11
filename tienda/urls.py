
from django.contrib import admin
from django.urls import path,include
from django.views.decorators.http import require_GET, require_POST
from .views import vistaTienda,DetalleArticulo,marca,compraEnvios,listadoCarrito,ProductoViewset,agradecimiento,filtroProductos
from rest_framework import routers


router = routers.DefaultRouter()
router.register('producto',ProductoViewset)

urlpatterns = [
    path('', vistaTienda,name='tienda'),
    path('carrito/<int:pk>', DetalleArticulo.as_view(),name='carrito'),
    path('filtroProductos/', filtroProductos,name='filtroProductos'),
    path('listadoCarrito/',listadoCarrito,name='listadoCarrito'),
    path('compraEnvios/', compraEnvios,name='compraEnvios'),
    path('agradecimiento/', agradecimiento,name='agradecimiento'),
    path('marca/<int:marca_id>', marca,name='marca'),
    path('api/',include(router.urls))
]
