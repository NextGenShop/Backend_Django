from django.db import models


# Create your models here.
class BasketDB(models.Model):
    basketId = models.AutoField(primary_key=True)
    shopperId = models.IntegerField(unique=True, null=False)
    totalPrice = models.FloatField(default=0, null=True)
    isEmpty = models.BooleanField(default=True, null=True)


class BasketItem(models.Model):
    basketItemId = models.AutoField(primary_key=True)
    basketId = models.IntegerField(null=False)
    productId = models.IntegerField()
    quantity = models.IntegerField()
