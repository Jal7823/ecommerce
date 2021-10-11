from django.contrib import admin
from .models import Order,OrderLine

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','completed',)
    list_filter = ('user','completed',)


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('user','product','order','cantidad',)
    list_filter = ('user','product','order','cantidad',)




admin.site.register(Order,OrderAdmin)
admin.site.register(OrderLine,OrderLineAdmin)