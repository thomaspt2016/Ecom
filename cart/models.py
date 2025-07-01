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
    