from cart.models import order
from django import forms

class Orderform(forms.ModelForm):
    class Meta:
        model = order
        Payment_Method = forms.CharField(widget=forms.RadioSelect(choices=order.paymentchoic))
        fields = ['address', 'phonenum','Payment_Method',]
        labels = {
            'address': 'Delivery Address',
            'phonenum': 'Contact Phone Number',
            'payment_method': 'Select Payment Method',
        }