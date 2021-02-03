from django.db import models


# Create your models here.
class BasketDB(models.Model):
    basketID = models.CharField(max_length=100, primary_key=True)
    shopper = models.IntegerField()
    items = models.TextField(null=True)
    totalPrice = models.FloatField()


class BasketItem(models.Model):
    basketItemID = models.AutoField(primary_key=True)
    basketID = models.IntegerField()
    productID = models.IntegerField()
    quantity = models.FloatField()
