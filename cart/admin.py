from django.contrib import admin

from cart.models import Cart, Favorite


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_filter = ('user', 'product')
    search_fields = ('user', 'product')


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('user', 'product')
    search_fields = ('user', 'product')



admin.site.register(Cart, CartAdmin)
admin.site.register(Favorite, FavoriteAdmin)