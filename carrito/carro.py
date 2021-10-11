from django.shortcuts import redirect



class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart


    def add(self, producto):
        


        if (str(producto.id) not in self.cart.keys()):
            self.cart[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'cantidad': 1,
                'precio': str(producto.precio),
                'precioMayor': str(producto.precioMayor),
                'imagen': producto.imagen.url
            }
        
        else:
            for key, value in self.cart.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] + 1

                    break

        self.guardar()  

    def guardar(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.guardar()

    def decrement(self, producto):
        for key, value in self.cart.items():
            if key == str(producto.id):
                value['cantidad'] = value['cantidad']-1
                if value['cantidad'] < 1:
                    self.remove(producto)
                break
                    
        self.guardar()
                
    def clear(self,):
        self.session['cart'] = {}
        self.session.modified = True

