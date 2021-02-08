from django.db import models


# Create your models here.
class ShopperDB(models.Model):
    shopperId = models.AutoField(primary_key=True)
    shopperEmail = models.EmailField()
    shopperPassword = models.CharField(max_length=128)
    shopperName = models.CharField(max_length=50)
    shopperPhone = models.CharField(max_length=15)
    shopperAddress = models.TextField()

    def __str__(self):
        return self.shopperName
