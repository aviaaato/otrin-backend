from django.shortcuts import render

from rest_framework import generics

from .models import Category, Product
from .serializers import CategorySerializer, ProductListSerializer, ProductCreationSerializer

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreationSerializer

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return ProductCreationSerializer

        elif self.request.method == 'GET':
            return ProductListSerializer