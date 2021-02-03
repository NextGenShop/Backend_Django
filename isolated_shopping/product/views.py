from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import NotFound
from .models import ProductDB
from .serializer import ProductSerializer
import django_filters


# Create your views here.
# product search and add
# api: localhost:8000/product
class ProductSearch(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    def get_queryset(self):
        queryset = ProductDB.objects.all()
        keyword = self.request.query_params.get('name', None)
        if keyword is not None and len(keyword) != 0 and keyword.isspace() is not True:
            return queryset.filter(name__icontains=keyword)
        else:
            raise ValidationError({"msg": ["Parameter Error"]})


# get products by retailer
# test api: localhost:8000/product/retailer/<str:pk>
class ProductSearchRetailer(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        queryset = ProductDB.objects.all()
        keyword = self.kwargs.get(self.lookup_url_kwarg)
        if keyword is not None and len(keyword) != 0 and keyword.isspace() is not True:
            return queryset.filter(soldBy__icontains=keyword)
        else:
            raise ValidationError({"msg": ["Parameter Error"]})


# get product information by ProductID
# test api: localhost:8000/product/<int:pk>
class GetProductById(generics.ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        keyword = self.kwargs.get(self.lookup_url_kwarg)
        if keyword is not None:
            queryset = ProductDB.objects.filter(productID=keyword).exists()
            if queryset is True:
                return ProductDB.objects.filter(productID=keyword)
            else:
                raise NotFound({"msg": ["Product ID does not exist"]})
        else:
            raise ValidationError({"msg": ["Parameter Error"]})
