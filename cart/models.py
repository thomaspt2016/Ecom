from django.db import models
from shop.models import Product,category
from loginfo.models import CustomUser as Cus


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(Cus, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

    def total_price(self):
        return self.qty * self.product.price

class order(models.Model):
    user = models.ForeignKey(Cus, on_delete=models.CASCADE)
    address = models.TextField()
    phonenum = models.IntegerField()
    paymentchoic = (
        ('COD','cash on delivery'),
        ('online payment','online payment'),
    )
    Payment_Method = models.CharField(max_length=100)
    order_Id = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=False)
    amount = models.IntegerField(default=0)
    def __str__(self):
        return str(self.order_Id)

class OrderItems(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    def __str__(self):
        return str(self.order.order_Id)
