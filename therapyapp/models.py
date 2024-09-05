from enum import unique

from django.db import models
from django.db.models import CharField, PROTECT


class Direction(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название направления')
    content = models.TextField(blank=True, verbose_name='Описание категории')
    image = models.ImageField(upload_to='photos/direction/%Y/%m/%d', verbose_name='Фото', blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направления товаров'
        verbose_name_plural = 'Направления товаров'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    content = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='photos/category/%Y/%m/%d', verbose_name='Фото', blank=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')
    direction = models.ForeignKey('Direction', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='photos/product/%Y/%m/%d')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    manufacturer = models.CharField(max_length=100, verbose_name='Производитель')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    price = models.FloatField()
    direction = models.ForeignKey('Direction', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


class Worker(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    post = models.CharField(max_length=50, verbose_name='Должность')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    e_mail = models.CharField(max_length=50, verbose_name='Email')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудники'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name']


class CooperationRequest(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    company_name = models.CharField(max_length=120, verbose_name='Компания')
    e_mail = models.CharField(max_length=100, verbose_name='Email')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    content = models.CharField(verbose_name='Доп информация')
