from django.shortcuts import render
from .models import Producto

# Create your views here.



def vistaProductos(request):
    return render(request,'productos/productos.html')


def home(request):
    catg = Producto.objects.filter(parent=None)
    context = {'catg':catg}    
    return render(request, 'index.html', context)