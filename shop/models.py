import uuid

from django.db import models

from sorl.thumbnail import ImageField, get_thumbnail


class Category(models.Model):
    objects = None
    id = models.SlugField(max_length=150, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Категории'  # Настройка для наименования набора объектов
        ordering = ('name',)


NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    objects = None
    id = models.SlugField(max_length=150, primary_key=True, verbose_name='id')
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')
    image_preview = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=1, **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    purchase_price = models.IntegerField('цена за покупку')
    date_creation = models.DateField(max_length=150, verbose_name='дата создания')
    date_last_mod = models.DateField(max_length=150, verbose_name='дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Товары'  # Настройка для наименования набора объектов
        ordering = ('name',)
