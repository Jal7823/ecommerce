from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from productos.models import Producto
from .carro import Cart
from .deseos import Deseos
from django.contrib import messages
from django.core.paginator import Paginator


# CARRITO
def add_product(request,producto_id):


    cart = Cart(request)
    producto = Producto.objects.get(id= producto_id)
    cart.add(producto=producto)
    convertido = str (producto_id)
    messages.success(request,'Producto agregado al carrrito!')

    # capura el url antes de agregar al carrito y redireccionamos alli

    try:
        urlAnterior = request.META.get('HTTP_REFERER')
    except :
        urlAnterior = 'index'

    return redirect(urlAnterior)

def remove_product(request,producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id= producto_id)
    cart.remove(producto=producto)

    try:
        urlAnterior = request.META.get('HTTP_REFERER')
    except :
        urlAnterior = 'index'

    return redirect(urlAnterior)
    
def decrement_product(request,producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id= producto_id)
    cart.decrement(producto=producto)
    messages.success(request,'Producto eliminado del carrito!')
    try:
        urlAnterior = request.META.get('HTTP_REFERER')
    except :
        urlAnterior = 'index'

    return redirect(urlAnterior)

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    try:
        urlAnterior = request.META.get('HTTP_REFERER')
    except :
        urlAnterior = 'index'

    return redirect(urlAnterior)

