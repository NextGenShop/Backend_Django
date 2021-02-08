"""isolated_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product import views as p_views
from shopping_basket import views as sb_views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('product/', p_views.ProductProcess.as_view(), name='product_process'),
    path('product/<int:pk>', p_views.GetProductById.as_view(), name='get_product_by_ID'),
    path('product/retailer/<str:pk>/', p_views.ProductSearchRetailer.as_view(), name='product_query_by_retailer'),
    # path('basket/shopper/<int:pk>', sb_views.GetBasketByShopperId.as_view(), name='basket_query_by_shopper'),
    # path('basket/', sb_views.BasketPost.as_view(), name='basket_add'),
    # path('basket/<int:pk>', sb_views.BasketUpdate.as_view(), name='basket_update'),
    path('basket/<int:pk>', sb_views.BasketProcess.as_view(), name='basket_process'),
]
