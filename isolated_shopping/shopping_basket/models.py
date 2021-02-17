from django.db import models


# Create your models here.
class BasketDB(models.Model):
    shopperId = models.IntegerField(primary_key=True, unique=True, null=False)
    items = models.CharField(max_length=100, null=True)
    totalPrice = models.FloatField()


class BasketItem(models.Model):
    basketItemId = models.AutoField(primary_key=True)
    shopperId = models.IntegerField()
    productId = models.IntegerField()
    quantity = models.IntegerField()
