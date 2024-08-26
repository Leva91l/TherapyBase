from django.contrib import admin

from therapyapp.models import Category, Product, Worker


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'image')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'content')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'post', 'phone', 'e_mail')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductsAdmin)
admin.site.register(Worker, WorkerAdmin)
