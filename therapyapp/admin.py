from django.contrib import admin

from therapyapp.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'image')
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)