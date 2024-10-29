from django.template.context_processors import request
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser, AllowAny

from api.permissions import IsAdminOrReadOnly
from api.serializers import ProductSerizliser, CategorySerizliser, FavoriteSerializer, CartSerializer
from cart.models import Favorite, Cart
from therapyapp.models import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerizliser
    permission_classes = (IsAdminOrReadOnly,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerizliser
    permission_classes = (IsAdminOrReadOnly,)


class ProductsByCategoryViewSet(ListModelMixin, GenericAPIView):
    serializer_class = ProductSerizliser
    permission_classes = (IsAdminOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Product.objects.filter(category=pk)

    def get(self, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)


