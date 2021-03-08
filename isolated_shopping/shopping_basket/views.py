from .models import BasketDB, BasketItem
from shopper.models import ShopperDB
from .serializers import ShoppingBasketSerializer, ShoppingBasketModifySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BasketProcess(APIView):
    @staticmethod
    def object_check(pk):
        check = BasketDB.objects.filter(shopperId=pk).exists()
        if check:
            return BasketDB.objects.filter(shopperId=pk)
        else:
            return check

    @staticmethod
    def shopper_check(pk):
        check = ShopperDB.objects.filter(shopperId=pk).exists()
        if check:
            return True
        else:
            return False

    @staticmethod
    def delete_method(pk):
        basket = BasketDB.objects.filter(shopperId=pk)
        if basket.exists():
            basket_id = basket[0].basketId
            BasketItem.objects.filter(basketId=basket_id).delete()
            basket.update(isEmpty=True)
            basket.update(totalPrice=0)
            return True
        else:
            return False

    def get(self, request, pk):
        query_check = self.object_check(pk=pk)
        if not query_check:
            return Response(data={"msg": "Basket associated with Shopper ID not found"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            query_data = ShoppingBasketSerializer(instance=query_check[0], many=False)
            return Response(query_data.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query_check = self.object_check(pk=pk)
        if not query_check:
            if self.shopper_check(pk=pk):
                create_data = ShoppingBasketModifySerializer(data=request.data, partial=True)  # Create basket if not exist
                if create_data.is_valid():
                    create_data.save(shopperId=pk)
                    serialised_data = ShoppingBasketSerializer(instance=create_data.instance, many=False)
                    return Response(data=serialised_data.data, status=status.HTTP_200_OK)
                else:
                    return Response(data={"msg": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={"msg": "Shopper ID not found"}, status=status.HTTP_404_NOT_FOUND)
        else:  # Update existing basket
            update_data = ShoppingBasketModifySerializer(instance=query_check[0], data=request.data, partial=True)
            if update_data.is_valid():
                update_data.save()
                serialised_data = ShoppingBasketSerializer(instance=update_data.instance, many=False)
                return Response(data=serialised_data.data, status=status.HTTP_200_OK)
            else:
                return Response(data={"msg": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        delete_status = self.delete_method(pk=pk)
        if not delete_status:
            return Response(data={"msg": "Basket associated with Shopper ID not found"},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
