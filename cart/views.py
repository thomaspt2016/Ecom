from django.shortcuts import render,redirect
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

class CartReductionView(View):
     def get(self, request, i):
        u = request.user
        prod = Product.objects.get(id=i)
        pro = Cart.objects.get(product=prod,user=u)    
        pro.qty -= 1
        pro.save()
        return redirect('cart:cartview')

class DeleteItemView(View):
     def get(self, request, i):
        u = request.user
        prod = Product.objects.get(id=i)
        pro = Cart.objects.get(product=prod,user=u)  
        pro.delete()
        return redirect('cart:cartview')

class QtyUpdateCartView(View):
    def get(self, request, i):
        u = request.user
        prod = Product.objects.get(id=i)
        pro = Cart.objects.get(product=prod, user=u)
        pro.qty += 1
        pro.save()
        return redirect('cart:cartview')

class OrderformView(View):
    def get(self, request):
        return HttpResponse("Orderform")