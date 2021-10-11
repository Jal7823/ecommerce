from django.shortcuts import redirect

class Deseos:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cartDeseos = self.session.get("cartDeseos")
        if not cartDeseos:
            cartDeseos = self.session["cartDeseos"] = {}
        self.cartDeseos = cartDeseos

    def add(self, producto):
        if (str(producto.id) not in self.cartDeseos.keys()):
            self.cartDeseos[producto.id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'cantidad': 1,
                'precio': str(producto.precio),
                'imagen': producto.imagen.url
            }
            

        else:
            for key, value in self.cartDeseos.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] + 1

                    break

        self.guardar()  

    def guardar(self):
        self.session['cartDeseos'] = self.cartDeseos
        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cartDeseos:
            del self.cartDeseos[producto_id]
            self.guardar()

    def decrement(self, producto):
        for key, value in self.cartDeseos.items():
            if key == str(producto.id):
                value['cantidad'] = value['cantidad']-1
                if value['cantidad'] < 1:
                    self.remove(producto)
                break
                    
        self.guardar()
                

    def clear(self):
        self.session['cartDeseos'] = {}
        self.session.modified = True
