from django.contrib import admin
from django.utils.safestring import mark_safe

from therapyapp.models import Category, Product, Worker


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'image')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'content', 'show_image')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def show_image(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    show_image.__name__ = 'Фото'


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'post', 'phone', 'e_mail')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(Worker, WorkerAdmin)
