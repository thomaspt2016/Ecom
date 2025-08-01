from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from shop.models import Product,category
from cart.models import Cart,order,OrderItems
from cart.forms import Orderform
import razorpay
from loginfo.models import CustomUser as cus
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
        us = request.user
        cartpr = Cart.objects.filter(user = us)
        billinform = Orderform()
        return render(request, 'checkout.html',{'form':billinform,'cart':cartpr})
    def post(self, request):
        us = request.user
        billinform = Orderform(request.POST)
        if billinform.is_valid():
            ordobj =billinform.save(commit=False)
            ordobj.user = us
            ordobj.save()
            c = Cart.objects.filter(user = us)
            total = 0
            for i in c:
                o = OrderItems.objects.create(qty = i.qty,product=i.product,order = ordobj)
                o.save()
                total +=i.qty*i.product.price 
        if ordobj.Payment_Method == 'online payment':
            client = razorpay.Client(auth=("rzp_test_sJgGk1sHeX3AWm", "ylWAgRlJ3cxLO4BG25C7YEAX"))
            responsepayement = client.order.create(dict(amount=int(total*100), currency="INR"))
            # print(responsepayement)
            ordid = responsepayement['id']
            ordobj.order_Id = ordid
            ordobj.is_ordered = False
            ordobj.save()
            return render(request,'payment.html',{'payment':responsepayement,'name':us.username})
        else:
            ordobj.is_ordered = True
            ordobj.save()
            return HttpResponse ("dsfsdf m")
    

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login

@method_decorator(csrf_exempt, name='dispatch')
class PaymentScucess(View):
    def post(self,request,i):
        usr = cus.objects.get(username =i)
        login(request, usr)
        res = request.POST
        o = order.objects.get(order_Id = res['razorpay_order_id'])
        o.is_ordered = True
        o.save()
        items = OrderItems.objects.filter(order = o)
        for i in items:
            i.product.qty -= i.qty
            i.product.save()

        return render(request,'paysuccess.html')