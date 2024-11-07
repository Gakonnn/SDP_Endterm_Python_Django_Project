from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'tags']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_email', 'status']
