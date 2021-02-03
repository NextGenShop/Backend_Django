from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import NotFound
from .models import BasketDB, BasketItem
from .serializers import ShoppingBasketSerializer,ShoppingBasketWriteSerializer
import django_filters


# Create your views here.
# get a shopping basket by shopping id
# api: localhost:8000/basket/shopper/<int:pk>
class GetBasketByShopperId(generics.ListAPIView):
    serializer_class = ShoppingBasketSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        keyword = self.kwargs.get(self.lookup_url_kwarg)
        if keyword is not None:
            queryset = BasketDB.objects.filter(shopper=keyword).exists()
            if queryset is True:
                return BasketDB.objects.filter(shopper=keyword)
            else:
                raise NotFound({"msg": ["Shopping Basket does not exist"]})
        else:
            raise ValidationError({"msg": ["Parameter Error"]})


class BasketPost(generics.CreateAPIView):
    serializer_class = ShoppingBasketWriteSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    queryset = BasketDB.objects.get_queryset().all()


class BasketUpdate(generics.UpdateAPIView):
    serializer_class = ShoppingBasketWriteSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    lookup_url_kwarg = "pk"
    queryset = BasketDB.objects.all()
