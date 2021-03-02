from django.db import models


# Create your models here.
class ProductDB(models.Model):
    productId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.TextField(null=True)
    price = models.FloatField()
    stock = models.PositiveIntegerField(default=1)
    retailer = models.CharField(max_length=100)
    views = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name
