from rest_framework import routers

from api.views import ProductViewSet, CategoryViewSet, FavoriteViewSet, CartViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='api_products')
router.register(r'categories', CategoryViewSet)
router.register('favorite', FavoriteViewSet)
router.register(r'cart', CartViewSet)

