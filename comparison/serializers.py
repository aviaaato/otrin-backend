from rest_framework import serializers

from .models import (
    Category, 
    Product, 
    Store,
    Location, 
    Price,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image', 'category')


class ProductCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'image', 'category', 'moderator')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Store
        fields = ('id', 'name', 'address', 'location', )

    def create(self, validated_data):
        location = validated_data.pop('location')
        location = Location.objects.create(**location)
        store = Store.objects.create(**validated_data, location=location)

        return store


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ('value', 'product', 'store')