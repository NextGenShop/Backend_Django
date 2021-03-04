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
        item_list = BasketItem.objects.filter(shopperId=shopper_id).all()
        basket_items = []
        for item in item_list:
            item_info = ProductDB.objects.filter(productId=item.productId).all()
            # item_information = item_info[0]
            # item_dict = {"product": {"productId": item_information.productId, "name": item_information.name,
            #                          "image": item_information.image, "price": item_information.price,
            #                          "stock": item_information.stock, "soldBy": item_information.soldBy},
            #              "quantity": item.quantity}
            item_dict = {"product": ProductSerializer(item_info[0]).data,
                         "quantity": item.quantity}
            basket_items.append(item_dict)
        return basket_items

    def get_shopper(self, obj):
        shopper_id = obj.shopperId
        shoppers = ShopperDB.objects.filter(shopperId=shopper_id).all()
        shopper_information = []
        for shopper_info in shoppers:
            # shopper_dict = {"shopperId": shopper_info.shopperId, "shopperEmail": shopper_info.shopperEmail,
            #                 "shopperName": shopper_info.shopperName, "shopperPhone": shopper_info.shopperPhone,
            #                 "shopperAddress": shopper_info.shopperAddress}
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
            totalPrice=0
        )
        sum_price = 0
        items = validated_data["items"]
        for item in items:
            BasketItem.objects.create(
                shopperId=validated_data["shopperId"],
                productId=item["product"]["productId"],
                quantity=item["quantity"]
            )
            sum_price = sum_price + item["quantity"] * ProductDB.objects.get(productId=item["product"]["productId"]).price
        basket.totalPrice = sum_price
        basket.save()
        return basket

    def update(self, instance, validated_data):
        current_shopper_id = instance.shopperId

        sum_price = 0
        BasketItem.objects.filter(shopperId=current_shopper_id).delete()
        items = validated_data["items"]
        for item in items:
            BasketItem.objects.create(
                shopperId=current_shopper_id,
                productId=item["product"]["productId"],
                quantity=item["quantity"]
            )
            sum_price = sum_price + item["quantity"] * ProductDB.objects.get(productId=item["product"]["productId"]).price
        instance.totalPrice = sum_price
        instance.save()

        return instance
