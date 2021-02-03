from django.contrib import admin
from .models import ProductDB


# Register your models here.
@admin.register(ProductDB)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price', 'stock', 'soldBy')
    search_fields = list_display
    list_filter = list_display
