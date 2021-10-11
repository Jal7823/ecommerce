from django.contrib import admin
from django.urls import path,include
from .views import vistaProductos

urlpatterns = [
    path('', vistaProductos,name='productos'),
]
