from django.db import models


class Category(models.Model):
    objects = None
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
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')
    image_preview = models.ImageField(upload_to='image', height_field=None, width_field=None, max_length=1, **NULLABLE)
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


class Blogs(models.Model):
    objects = None
    title = models.CharField(max_length=150, verbose_name='наименование')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    content = models.CharField(max_length=150, verbose_name='содержимое')
    image_preview = models.ImageField(upload_to='image_blogs', height_field=None, width_field=None, max_length=1, **NULLABLE)
    creation_date = models.DateField(max_length=150, verbose_name='дата создания')
    publication_attribute = models.BooleanField(default=True, verbose_name='признак публикации')
    number_of_views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Блоги'  # Настройка для наименования набора объектов
