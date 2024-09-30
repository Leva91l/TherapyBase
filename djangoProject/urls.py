"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

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

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
