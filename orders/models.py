from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F,Sum,FloatField
from productos.models import Producto
from usuarios.models import Usuario

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property

    def total(self):
        return self.orderline_set.aggregate(
            total = Sum(F('product__precio')*F('cantidad'),output_field=FloatField())
        )['total'] or FloatField(0)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

class OrderLine(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Producto,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    cantidad = models.IntegerField(default =1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.cantidad} de {self.product}'


    class Meta:
        db_table = 'orderlines'
        verbose_name = 'Linea de pedido'
        verbose_name_plural = 'Lineas de pedidos'
        ordering = ['id']

