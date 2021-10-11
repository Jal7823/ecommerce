from productos.models import Producto,Marca
from rest_framework import serializers

class ProductoSerializers(serializers.ModelSerializer):
    class  Meta:
        model = Producto
        fields = '__all__'