from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import CODE_LENGTH
from shop.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    verification_code = models.CharField(max_length=100, verbose_name='код верификации', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='верифицирован')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class ConfirmationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=CODE_LENGTH)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []