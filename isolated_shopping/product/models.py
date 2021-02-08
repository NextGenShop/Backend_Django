from django.db import models
from retailer.models import RetailerDB


# Create your models here.
class ProductDB(models.Model):
    productId = models.AutoField(primary_key=True)
    soldBy = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.TextField(null=True)
    price = models.FloatField()
    stock = models.FloatField()

    def __str__(self):
        return self.name
