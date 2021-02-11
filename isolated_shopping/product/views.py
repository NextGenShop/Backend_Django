from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import NotFound
from .models import ProductDB
from .serializer import ProductSerializer
import django_filters


# Create your views here.
# product search and add
# api: localhost:8000/product
class ProductProcess(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    def get_queryset(self):
        queryset = ProductDB.objects.all()
        query = self.request.query_params.get('query', None)
        retailer = self.request.query_params.get('retailer', None)
        limit = self.request.query_params.get('limit', None)

        if query is not None and len(query) != 0 and query.isspace() is not True:
            if query.isdigit():
                queryset_query = queryset.filter(name__icontains=query).union(queryset.filter(productId=query))
            else:
                queryset_query = queryset.filter(name__icontains=query)
            if retailer is not None and len(retailer) != 0 and retailer.isspace() is not True:
                if limit is not None and limit.isdigit():
                    limit = int(limit)
                    return queryset_query.intersection(queryset.filter(retailer__icontains=retailer))[:limit]
                else:
                    return queryset_query.intersection(queryset.filter(retailer__icontains=retailer))
            else:
                if limit is not None and limit.isdigit():
                    limit = int(limit)
                    return queryset_query[:limit]
                else:
                    return queryset_query
        elif retailer is not None and len(retailer) != 0 and retailer.isspace() is not True:
            if limit is not None and limit.isdigit():
                limit = int(limit)
                return queryset.filter(retailer__icontains=retailer)[:limit]
            else:
                return queryset.filter(retailer__icontains=retailer)
        else:
            raise ValidationError({"msg": ["Parameter Error"]})
