import json

from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Category, Product, Store, Price
from .serializers import (
    CategorySerializer, 
    ProductListSerializer, 
    ProductCreationSerializer,
    StoreSerializer,
    PriceSerializer
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


class PriceView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

"""
    GET /product/{product_id}/prices
"""
class ProductPriceView(APIView):
    def get(self, request, pk, format=None):
        product = Product.objects.get(pk=pk)
        prices = Price.objects.filter(product=product.id)
        product_serializer = ProductListSerializer(product)
        product_data = json.loads(JSONRenderer().render(product_serializer.data))
        product_data['prices'] = []

        for price in prices:
            price_serializer = PriceSerializer(price)
            product_data['prices'].append(
                json.loads(JSONRenderer().render(price_serializer.data))
            )

        return Response(data=product_data)