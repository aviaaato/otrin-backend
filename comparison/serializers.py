from rest_framework import serializers

from .models import (
    Category,
    Product,
    Store,
    Location,
    Price,
    UserProfile,
    User
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'category')


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
    product = ProductListSerializer()
    store = StoreSerializer()

    class Meta:
        model = Price
        fields = ('value', 'product', 'store')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('moderator',)
        fields = ('email', 'password', 'first_name', 'last_name', 'profile')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        print(validated_data)
        profile_data = validated_data.pop('profile')

        password = validated_data.pop('password')
        user_profile = UserProfile(**validated_data)
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        # model = UserProfile
        fields = ('moderator',)
        # fields = ('email', 'password', 'first_name', 'last_name', 'profile')

    # def create(self, validated_data):
    #     print(validated_data)
    #     profile_data = validated_data.pop('profile')

    #     password = validated_data.pop('password')
    #     user_profile = UserProfile(**validated_data)
    #     user = User(**validated_data)
    #     user.set_password(password)
    #     user.save()

    #     return user