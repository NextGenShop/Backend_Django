from rest_framework import serializers
from .models import BasketDB, BasketItem
from shopper.models import ShopperDB
from product.models import ProductDB
from product.serializer import ProductSerializer
from shopper.serializer import ShopperSerializer


class ShoppingBasketSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    shopper = serializers.SerializerMethodField()

    class Meta:
        model = BasketDB
        fields = ("shopper", "items", "totalPrice")

    def get_items(self, obj):
        shopper_id = obj.shopperId
        basket = BasketDB.objects.get(shopperId=shopper_id)
        basket_id = basket.basketId
        tag = basket.isEmpty
        basket_items = []
        if tag:
            return basket_items
        item_list = BasketItem.objects.filter(basketId=basket_id).all()
        for item in item_list:
            item_info = ProductDB.objects.filter(productId=item.productId).all()
            item_dict = {"product": ProductSerializer(item_info[0]).data,
                         "quantity": item.quantity}
            basket_items.append(item_dict)
        return basket_items

    def get_shopper(self, obj):
        shopper_id = obj.shopperId
        shoppers = ShopperDB.objects.filter(shopperId=shopper_id).all()
        shopper_information = []
        for shopper_info in shoppers:
            shopper_dict = ShopperSerializer(shopper_info).data
            shopper_information.append(shopper_dict)
        return shopper_information


class ShoppingBasketModifySerializer(serializers.ModelSerializer):
    items = serializers.ListField()

    class Meta:
        model = BasketDB
        fields = ("shopperId", "items", "totalPrice")

    def create(self, validated_data):
        basket = BasketDB.objects.create(
            shopperId=validated_data["shopperId"],
            isEmpty=False,
            totalPrice=0
        )
        sum_price = 0
        items = validated_data["items"]
        for item in items:
            BasketItem.objects.create(
                basketId=basket.basketId,
                productId=item["product"]["productId"],
                quantity=item["quantity"]
            )
            product = ProductDB.objects.filter(productId=item["product"]["productId"])[0]
            product_price = product.price
            product.views = product.views + 1
            product.save()
            sum_price = sum_price + item["quantity"] * product_price
        basket.totalPrice = sum_price
        basket.save()
        return basket

    def update(self, instance, validated_data):
        basket_id = instance.basketId
        BasketItem.objects.filter(basketId=basket_id).delete()
        items = validated_data["items"]
        sum_price = 0
        for item in items:
            BasketItem.objects.create(
                basketId=basket_id,
                productId=item["product"]["productId"],
                quantity=item["quantity"]
            )
            product = ProductDB.objects.filter(productId=item["product"]["productId"])[0]
            product_price = product.price
            product.views = product.views + 1
            product.save()
            sum_price = sum_price + item["quantity"] * product_price
        instance.totalPrice = sum_price
        instance.isEmpty = False
        instance.save()

        return instance
