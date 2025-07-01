from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)
    descrip = models.TextField()
    image = models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    descrip = models.TextField()
    image = models.ImageField(upload_to='product', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    availability = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)#only one time
    updated = models.DateField(auto_now=True)#will be updated every time
    category = models.ForeignKey(category, on_delete=models.CASCADE,related_name="products")#related name is for accessing from products to categor in this case

    def __str__(self):
        return self.name