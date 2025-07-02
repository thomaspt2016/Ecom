from cart.models import Cart
from shop.models import Product

def Incart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        co = 0
        totpri = 0
        for c in cart:
            co += c.qty
            prod = Product.objects.get(id=c.product.id)
            totpri += c.qty * prod.price

        return {'incart':cart,'qty':co,'Total':totpri}
    else:
        return {'incart':None}