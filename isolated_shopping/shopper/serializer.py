from rest_framework import serializers
from .models import ShopperDB


class ShopperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopperDB
        fields = ('shopperId', 'shopperEmail', 'shopperName', 'shopperPhone', 'shopperAddress')
