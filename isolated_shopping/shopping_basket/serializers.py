from rest_framework import serializers
from .models import BasketDB, BasketItem
from shopper.models import ShopperDB
from product.models import ProductDB


class ShoppingBasketSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    shopper = serializers.SerializerMethodField()

    class Meta:
        model = BasketDB
        fields = ("basketID", "shopper", "items", "totalPrice")

    def get_items(self, obj):
        basket_id = obj.basketID
        item_list = BasketItem.objects.filter(basketID=basket_id).all()
        basket_items = []
        for item in item_list:
            item_dict = {}
            item_info = ProductDB.objects.filter(productID=item.productID).all()
            for item_information in item_info:
                item_dict["productID"] = item_information.productID
                item_dict["name"] = item_information.name
                item_dict["image"] = item_information.image
                item_dict["price"] = item_information.price
                item_dict["stock"] = item_information.stock
                item_dict["soldBy"] = item_information.soldBy
            basket_items.append(item_dict)
        # print(basket_items)
        return basket_items

    def get_shopper(self, obj):
        shopper_id = obj.shopper
        shoppers = ShopperDB.objects.filter(shopperID=shopper_id).all()
        shopper_information = []
        for shopper_info in shoppers:
            shopper_dict = {"shopperID": shopper_info.shopperID, "shopperEmail": shopper_info.shopperEmail,
                            "shopperName": shopper_info.shopperName, "shopperPhone": shopper_info.shopperPhone,
                            "shopperAddress": shopper_info.shopperAddress}
            shopper_information.append(shopper_dict)
        return shopper_information


class ShoppingItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ("basketID",)

    def create(self, validated_data):
        products = validated_data["items"]
        print(products)
        for product in products:
            BasketItem(
                basketID=validated_data["basketID"],
                productID=product
            )


class ShoppingBasketWriteSerializer(serializers.ModelSerializer):
    # items = ShoppingItemWriteSerializer()
    items = serializers.ListField()

    class Meta:
        model = BasketDB
        fields = ("basketID", "shopper", "items", "totalPrice")

    def create(self, validated_data):
        basket = BasketDB.objects.create(
            basketID=validated_data["basketID"],
            shopper=validated_data["shopper"],
            totalPrice=validated_data["totalPrice"]
        )
        items = validated_data["items"]
        print(items)
        for item in items:
            BasketItem.objects.create(
                basketID=validated_data["basketID"],
                productID=item["productID"],
                quantity=item["quantity"]
            )
        return basket

    def update(self, instance, validated_data):
        instance.shopper = validated_data.get("shopper", instance.shopper)
        instance.totalPrice = validated_data.get("totalPrice", instance.totalPrice)
        instance.save()

        BasketItem.objects.filter(basketID=validated_data["basketID"]).delete()
        items = validated_data["items"]
        for item in items:
            BasketItem.objects.create(
                basketID=validated_data["basketID"],
                productID=item["productID"],
                quantity=item["quantity"]
            )
        return instance
