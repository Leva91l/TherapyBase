from django.contrib.auth.models import User
from rest_framework import serializers

from cart.models import Favorite, Cart
from therapyapp.models import Product, Category


class CategorySerizliser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerizliser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Favorite
        fields = ('user', 'product', 'product_name')


class CartsSerializer:
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects)
    quantity = serializers.IntegerField(default=0)
    price = serializers.FloatField(default=0)
    # created_timestamp = serializers.DateTimeField(auto_now_add=True)

class CartSerializer(CartsSerializer, serializers.ModelSerializer):
    price = serializers.FloatField(source='product.price', read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'
