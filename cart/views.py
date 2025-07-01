from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from shop.models import Product,category
from cart.models import Cart

# Create your views here.

class AddtoCart(View):
    def get(self, request,i):
        u = request.user
        p = Product.objects.get(id = i)
        try:
            c = Cart.objects.get(user = u, product = p)
            c.qty += 1
            c.save()
        except:
            c = Cart(user = u, product = p, qty = 1)
            c.save()
        return render(request, 'cart.html')
    
class CartView(View):
    def get(self,request):
        u = request.user
        c = Cart.objects.filter(user = u)
        return render(request, 'cart.html', {'cart':c})
