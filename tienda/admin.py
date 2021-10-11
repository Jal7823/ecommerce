from django.contrib import admin
from .models import TituloPag,CheckoutClientes

# Register your models here.


class TituloPagAdmin(admin.ModelAdmin):
    list_display = ('id','titulo',)



class CheckoutClientesAdmin(admin.ModelAdmin):
    search_fields = ('id','nombre','apellido','dni','direc','loc','pcia','tlf','transp') 
    list_display = ('id','nombre','apellido','dni','direc','loc','pcia','tlf','transp')
    list_filter = ('id','nombre','apellido','dni','direc','loc','pcia','tlf','transp')
    ordering = ('id',)


admin.site.register(TituloPag,TituloPagAdmin)
admin.site.register(CheckoutClientes,CheckoutClientesAdmin)
