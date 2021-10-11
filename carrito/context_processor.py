from carrito. carro import Cart




def importe_total(request):
    total = 0.0 



    if request.user.is_active:


        if 'cart' in request.session:
            cantidadArt = []
            for key ,value in request.session['cart'].items() :


                cantidadArt.append(value['cantidad'])
                sumando = sum(cantidadArt)

                if sumando >= 6 or value['cantidad'] >= 3 :
                    subtotal = total +(float(value['precioMayor'])*value['cantidad'])
                    total = round(subtotal,2)

                else:
                    subtotal = total +(float(value['precio'])*value['cantidad'])
                    total = round(subtotal,2)
        else:
            for key ,value in request.session['cart'].items():
                subtotal = total +(float(value['precio'])*value['cantidad'])
                total = round(subtotal,2)




    return {'importe_total':total}




    
