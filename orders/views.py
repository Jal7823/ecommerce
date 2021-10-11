from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Order,OrderLine
from tienda.models import CheckoutClientes
from carrito.carro import Cart
from carrito.context_processor import  importe_total
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario

#creacion de pedidos 


@login_required(login_url='login')
def process_order(request):
    order = Order.objects.create(user=request.user,completed = True) #creamos un pedido pasandole el usuario y modificando la propiedad completado
    cart = Cart(request) #habilitamos el carrito
    order_lines = list()#creamos una lista para recorrerla


    for key,value in cart.cart.items(): #recorremos el carrito
        order_lines.append(
            OrderLine(
                product_id = key, #pasamos el id del producto
                cantidad = value['cantidad'], #pasamos la cantidad
                user = request.user, #pasamos el usuario
                order = order #pasamos el pedido
            )
        ) #toda esta informacion se pasa al bluk_create

    OrderLine.objects.bulk_create(order_lines) #se pasa toda la informacion recopilada por la lista 'order_line'

    pcia = request.user.pcia 
    consultaTotal = importe_total(request)
    total = consultaTotal['importe_total']




    #validacion de mono minimo para envio al interior y tipo de entrega

    if  pcia != 'C.A.B.A.' and total < 5000:
        print('==>envio al interior imposible por no alcanzar el monto minimo<==')
        messages.error(request,'Su pedido no fue procesado, el monto mínimo para envió al interior de país es $5000, por favor agregue mas productos')
        return redirect(to='listadoCarrito')

    else:        
        #envio de correo al cliente

        send_order_email( #aca se pasan los parameros a la funcion para enviar el correo
            order = order,
            order_lines = order_lines,
            username = request.user.username,
            user_email = request.user.email,
            nombre = request.user.nombre,
            apellido = request.user.apellido,
            dni = request.user.dni,
            direccion = request.user.direc,
            localidad = request.user.loc,
            provincia = request.user.pcia,
            telefono = request.user.tlf,
            transporte = request.user.transp,
        )

        # Cart.clear()

        messages.success(request,'Pedido creado con exito, mira nuestras novedades ')
        cart.clear()
        
        return redirect(to='agradecimiento')

def send_order_email(**kwargs):
    subject = 'Gracias por tu pedido' #asunto
    html_message = render_to_string('orders/envioEmails.html',{ #lo que va a contener el html
        'order':kwargs.get("order"),
        'order_lines': kwargs.get("order_lines"),
        'username':kwargs.get('username'),
        'apellido':kwargs.get('apellido'),
        'nombre':kwargs.get('nombre'),
        'dni':kwargs.get('dni'),
        'direccion':kwargs.get('direccion'),
        'localidad':kwargs.get('localidad'),
        'provincia':kwargs.get('provincia'),
        'telefono':kwargs.get('telefono'),
        'transporte':kwargs.get('transporte')
    })

    plain_message = strip_tags(html_message) #se guarda en una variable para el cotexto de send mail
    from_email = 'Departamento de ventas de Casa Nor-Ma' #quien envia el correo
    
    to = kwargs.get('user_email')# para quien se envia 


    send_mail(subject,plain_message,from_email,[to],html_message=html_message) #se pasa toda la info a la funcion que envia el pedido
    
def estiloMail(request):
    return render(request,'orders/envioEmails.html')


