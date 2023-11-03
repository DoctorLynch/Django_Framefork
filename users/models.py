from django.contrib.auth.models import AbstractUser
from django.db import models
from shop.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    verification_code = models.CharField(max_length=100, verbose_name='код верификации', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='верифицирован')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
