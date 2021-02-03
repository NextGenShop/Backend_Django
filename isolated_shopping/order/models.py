from django.db import models
from shopper.models import ShopperDB


# Create your models here.
class OrderDB(models.Model):
    orderID = models.AutoField(primary_key=True)
    orderedBy = models.ForeignKey(ShopperDB, related_name='orderedByWhom', on_delete=models.CASCADE)
    productsOrdered = models.TextField()
    totalPrice = models.FloatField()
    status = models.CharField(max_length=50)
