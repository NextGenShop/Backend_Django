from .models import BasketDB
from .serializers import ShoppingBasketSerializer, ShoppingBasketModifySerializer
# from rest_framework import generics
# from rest_framework.exceptions import ValidationError
# from rest_framework.exceptions import NotFound
# import django_filters

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
# get a shopping basket by shopping id
# api: localhost:8000/basket/shopper/<int:pk>
# class GetBasketByShopperId(generics.ListAPIView):
#     serializer_class = ShoppingBasketSerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#     lookup_url_kwarg = "pk"
#
#     def get_queryset(self):
#         keyword = self.kwargs.get(self.lookup_url_kwarg)
#         if keyword is not None:
#             queryset = BasketDB.objects.filter(shopper=keyword).exists()
#             if queryset is True:
#                 return BasketDB.objects.filter(shopper=keyword)
#             else:
#                 raise NotFound({"msg": ["Shopping Basket does not exist"]})
#         else:
#             raise ValidationError({"msg": ["Parameter Error"]})
#
#
# class BasketPost(generics.CreateAPIView):
#     serializer_class = ShoppingBasketModifySerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#     queryset = BasketDB.objects.get_queryset().all()
#
#
# class BasketUpdate(generics.UpdateAPIView):
#     serializer_class = ShoppingBasketModifySerializer
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#     lookup_url_kwarg = "pk"
#     queryset = BasketDB.objects.all()


class BasketProcess(APIView):

    @staticmethod
    def object_check(pk):
        check = BasketDB.objects.filter(shopperId=pk).exists()
        if check:
            return BasketDB.objects.filter(shopperId=pk)
        else:
            return check

    def get(self, request, pk):
        query_check = self.object_check(pk=pk)
        if not query_check:
            return Response(data={"msg": "Shopper ID not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            query_data = ShoppingBasketSerializer(instance=query_check[0], many=False)
            return Response(query_data.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query_check = self.object_check(pk=pk)
        if not query_check:
            return Response(data={"msg": "Shopper ID not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            update_data = ShoppingBasketModifySerializer(instance=query_check[0], data=request.data, partial=True)
            # return Response(data=update_data.data, status=status.HTTP_200_OK)
            if update_data.is_valid():
                update_data.save()
                return Response(data=update_data.data, status=status.HTTP_200_OK)
            else:
                return Response(data={"msg": "Invalid Input"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        query_check = self.object_check(pk=pk)
        if not query_check:
            return Response(data={"msg": "Shopper ID not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            query_check.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
