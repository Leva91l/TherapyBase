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
from django.contrib import admin

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from therapyapp.models import Direction
from therapyapp.views import *
from cart.views import *

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
    path('remove_quantity/<int:id>/', remove_quantity, name='remove_quantity'),
    path('favorite/', favorite, name='favorite'),

    path('favorite/<int:product_id>/', favorite_add, name='favorite_add'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
