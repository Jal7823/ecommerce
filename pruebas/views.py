from django.shortcuts import render,redirect
from django.db.models import Q
from productos.models import Producto,Marca,Genero



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

    print('\n==>',indiceCategoria,'\n')

    seleccionCategoriaFinal =[]
    for i  in indiceCategoria:
        seleccionCatego = (f'{i}')
        seleccionCategoriaFinal.append(seleccionCatego)

    print('\n==>',seleccionCategoriaFinal,'\n')

    categoriaFinal = ''
    for i in seleccionCategoriaFinal:
        categoriaSelect = request.GET.get(i)
        if categoriaSelect  :
            categoriaFinal = i

    print('\n==>',categoriaFinal,'\n')

    productos = Producto.objects.filter(
        Q(categoria__nombre__icontains=categoriaFinal),
    ).distinct()


    contexto = {
        'productos': productos,
        'categoria': categoria,
    }

    return render(request, 'pruebas/pruebas.html',contexto)
