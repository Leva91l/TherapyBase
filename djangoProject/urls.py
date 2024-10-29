from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from api.api_urls import router
from api.views import ProductsByCategoryViewSet
from cart.views import *
from therapyapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('products/<slug:prod_slug>/', ProductListView.as_view(), name='products'),
    path('product_info/<slug:prod_slug>/', ProductInfoView.as_view(), name='product_info'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('cooperation/', CooperationView.as_view(), name='cooperation'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('direction/<slug:dir_slug>/', CategoryView.as_view(), name='direction'),
    path('cart/', cart, name='cart'),
    path('cart_add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart_remove/<int:id>/', cart_remove, name='cart_remove'),
    path('add_quantity/<int:id>/', add_quantity, name='add_quantity'),
    path('add_quantity_man/', add_quantity_man, name='add_quantity_man'),
    path('remove_quantity/<int:id>/', remove_quantity, name='remove_quantity'),
    path('favorite/', favorite, name='favorite'),

    path('favorite_add/<int:product_id>/', favorite_add, name='favorite_add'),
    path('favorite_remove/<int:id>/', favorite_remove, name='favorite_remove'),
    path('search/', Search.as_view(), name='search'),
    path('delivery/', delivery, name='delivery'),
    path('found_nothing/', FoundNothing.as_view(), name='found_nothing'),
    path('about/', about, name='about'),
    path('send_mail/', send_to_manager, name='send_mail'),
    path('api/v1/', include(router.urls)),
    path('api/v1/products_by_categories/<int:pk>/', ProductsByCategoryViewSet.as_view(), name='products_by_category'),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#
