from django.urls import path
from .views import *

# app_name = 'Carro'

urlpatterns = [
    path('add_product/<int:producto_id>',add_product,name='add_product'),
    path('remove_product/<int:producto_id>',remove_product,name='remove_product'),
    path('decrement_product/<int:producto_id>',decrement_product,name='decrement_product'),
    path('clear_cart/',clear_cart,name='clear_cart'),

    
]