from django.shortcuts import render

from rest_framework import generics

from .models import Category, Product, Store
from .serializers import (
    CategorySerializer, 
    ProductListSerializer, 
    ProductCreationSerializer,
    StoreSerializer
)

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return ProductCreationSerializer

        elif self.request.method == 'GET':
            return ProductListSerializer


class StoreView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer