from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, **NULLABLE, verbose_name='описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Версия продукта', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Категории'  # Настройка для наименования набора объектов
        ordering = ('name',)


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')
    image_preview = models.ImageField(upload_to='image', height_field=None, width_field=None, max_length=100,
                                      **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    purchase_price = models.IntegerField('цена за покупку')
    date_creation = models.DateField(max_length=150, verbose_name='дата создания')
    date_last_mod = models.DateField(max_length=150, verbose_name='дата последнего изменения')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'Товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Товары'  # Настройка для наименования набора объектов
        permissions = [
            (
                'set_published',
                'Can publish posts'
            ),
        ]


class Blogs(models.Model):
    objects = None
    title = models.CharField(max_length=150, verbose_name='наименование')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.CharField(max_length=150, verbose_name='содержимое')
    image_preview = models.ImageField(upload_to='image_blogs', height_field=None, width_field=None, max_length=1,
                                      **NULLABLE)
    creation_date = models.DateField(max_length=150, verbose_name='дата создания')
    publication_attribute = models.BooleanField(default=True, verbose_name='признак публикации')
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Блоги'  # Настройка для наименования набора объектов


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    num_of_version = models.IntegerField(default=1, verbose_name='номер текущей версии', unique=True, **NULLABLE)
    name_version = models.CharField(max_length=150, verbose_name='название версии')
    flag_of_version = models.BooleanField(default=True, verbose_name='признак версии')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.product} {self.name_version}'

    class Meta:
        verbose_name = 'Версия'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Версии'  # Настройка для наименования набора объектов
