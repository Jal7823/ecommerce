from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


from productos.models import Producto
from .models import  CheckoutClientes



class FormItem(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class FromCheckout(forms.ModelForm):
    class Meta:
        model = CheckoutClientes
        fields = '__all__'


