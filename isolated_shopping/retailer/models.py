from django.db import models


# Create your models here.
class RetailerDB(models.Model):
    retailerID = models.AutoField(primary_key=True)
    retailerName = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
