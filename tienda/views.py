from django.http import request
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView,FormView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.contrib import messages
import random
from django.contrib.auth.decorators import login_required
from .serializers import ProductoSerializers
from rest_framework import viewsets
from carrito.carro import Cart
from .forms import FormItem, FromCheckout
from productos.models import Caracteristica, Producto, Marca,ImagenProducto,Caracteristica,Genero
from .models import TituloPag, CheckoutClientes
from orders.models import Order



# Create your views here.

# api
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers
# /api


def index(request):    
    cart = Cart(request)
    productos = Producto.objects.all()[:12]
    redondeo = Producto.objects.all()
    marca = Marca.objects.all()[0:4]     
    marcaConteo = Marca.objects.all().count()    
    nuevo = Producto.objects.all()[7:19]
    pagina = request.GET.get('buscador', 1)  # se captura la pagina actual o se igual a 1
    busqueda = request.GET.get('busqueda')  # se captura la pagina actual o se igual a 1

    # aleatorio = []
    # ordenado = aleatorio.sort()
    # for i in range(marcaConteo):
    #     resultado = random.randrange(0,marcaConteo)
    #     aleatorio.append(resultado)
        

    # extraccion = aleatorio[:2]

    # print(extraccion)
    # marca = Marca.objects.all()[extraccion[0]:extraccion[1]][0:4]     




    # filtros
    context ={
        'productos':productos,
        'marca':marca,
        'nuevo':nuevo,
        'busqueda':busqueda,
    }
    return render(request,'index.html', context)

class Base(ListView):
    model = Producto
    second_model = Marca
    queryset = Producto.objects.filter()
    context_object_name = 'producto', 'titulo'

class DetalleArticulo(DetailView):
    model = Producto  
    template_name = 'tienda/detalle.html'


    def get_context_data(self, **kwargs):
        context = super(DetalleArticulo, self).get_context_data(**kwargs)
        context['imagenAdicional'] = ImagenProducto.objects.all()
        context['marca'] = Marca.objects.all()
        context['categoria'] = Caracteristica.objects.filter(parent=None)


        contador = self.request.GET.get('contador')
        print(contador)

        if self.request.user.is_active:
            if 'cart' in self.request.session:
                for key ,value in self.request.session['cart'].items() :


                    # print('\nclave==>',key,'\nvalor',value) 

                    print('aca el carrito ==>',self.request.session['cart'].items(),'\n')
                    print('key ==>',key,'\n')
                    print('value ==>',value['producto_id'],'\n')

                    print('===========================================================')


        #aleatorio
        aleatorio = []

        for i in range(5):
            resultado = random.randrange(1,5)
            aleatorio.append(resultado)

        context['produc'] = Producto.objects.filter(marca = aleatorio[0])[:3]

        return context

def vistaTienda(request):
    productos = Producto.objects.all()
    titulo = TituloPag.objects.all()
    marca = Marca.objects.all()
    carro = Cart(request)

    #paginacion
    pagina = request.GET.get('page', 1)  # se captura la pagina actual o se igual a 1
    paginator = Paginator(productos, 12)  # despues de importado paginator se le dice cauntos va a mostrar por pagina
    productos = paginator.get_page(pagina)  # se captura la pagina actual
    pagina_actual = int(pagina)  # se pasa de string a int la pagina actual que viene del request
    paginas = range(1, productos.paginator.num_pages + 1)  # se itera el rango de paginas
    # buscador
    busqueda = request.GET.get('buscador')

    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains=busqueda)|
            Q(marca__categoria__icontains=busqueda)|
            Q(cod__icontains=busqueda),
        ).distinct()


    ###########filtro################
    categoria = Genero.objects.all()

    indiceCategoria = []
    for j in categoria:
            indiceCategoria.append(j)


    seleccionCategoriaFinal =[]
    for i  in indiceCategoria:
        seleccionCatego = (f'{i}')
        seleccionCategoriaFinal.append(seleccionCatego)


    categoriaFinal = ''
    for i in seleccionCategoriaFinal:
        categoriaSelect = request.GET.get(i)
        if categoriaSelect  :
            categoriaFinal = i

            productos = Producto.objects.filter(
                Q(categoria__nombre__icontains=categoriaFinal),
            ).distinct()
    

    contexto = {
        'productos': productos,
        'titulo': titulo,
        'marca': marca,
        'paginas': paginas,
        'pagina_actual': pagina_actual,
        'cart':Cart,
        'categoria': categoria,
    }



    

    return render(request, 'tienda/tienda.html', contexto)



def marca(request,marca_id):
    marca = Marca.objects.get(id=marca_id) #optenemos el id de la marca
    producto = Producto.objects.filter(marca=marca)#filtramos por el id optenido 
    
    busqueda = request.GET.get('buscador')

    if busqueda:
        producto = Producto.objects.filter(
            Q(nombre__icontains=busqueda)|
            Q(marca__marca__icontains=busqueda)|
            Q(cod__icontains=busqueda),
        ).distinct()

    contexto = {
        'marca':marca,
        'producto':producto
    }

    return render(request,'tienda/marca.html',contexto)

def compraEnvios(request):
    return render(request,'tienda/comprasEnvios.html')

def listadoCarrito(request):
    return render(request,'tienda/listado.html',)

def agradecimiento(request):

    return render(request, 'tienda/agradecimiento.html')

def filtroProductos(request):
    productos = Producto.objects.all()
    marcaConteo = Marca.objects.all().count()
    
    #busqueda general
    busqueda = request.GET.get('buscador')

    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains=busqueda)|
            Q(marca__categoria__icontains=busqueda)|
            Q(cod__icontains=busqueda),
        ).distinct()

    categoria = Genero.objects.all()

    indiceCategoria = []
    for j in categoria:
            indiceCategoria.append(j)


    seleccionCategoriaFinal =[]
    for i  in indiceCategoria:
        seleccionCatego = (f'{i}')
        seleccionCategoriaFinal.append(seleccionCatego)


    categoriaFinal = ''
    for i in seleccionCategoriaFinal:
        categoriaSelect = request.GET.get(i)
        if categoriaSelect  :
            categoriaFinal = i


    productos = Producto.objects.filter(
        Q(categoria__nombre__icontains=categoriaFinal),
    ).distinct()


    contexto = {
        'productos': productos,
        'categoria': categoria,
    }

    return render(request, 'tienda/filtro.html',contexto)

