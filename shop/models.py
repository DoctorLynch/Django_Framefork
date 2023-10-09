import uuid

from django.db import models


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
    image_preview = models.ImageField(upload_to='names/', verbose_name='изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
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