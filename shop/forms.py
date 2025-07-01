from shop.models import Product,category
from django import forms



class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model=category
        fields="__all__"