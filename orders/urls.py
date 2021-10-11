from django.contrib import admin
from django.urls import path, include
from  .views import process_order,estiloMail



urlpatterns = [
    path('', process_order,name='Pedido'),
    path('estiloMail', estiloMail,name='estiloMail'),
]