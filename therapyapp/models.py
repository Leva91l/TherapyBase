from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    content = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='photos/category/%Y/%m/%d', verbose_name='Фото', blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['name']