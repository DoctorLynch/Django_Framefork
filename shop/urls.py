from django.urls import path

from shop.apps import ShopConfig
from shop.views import base

app_name = ShopConfig.name

urlpatterns = [
    path('', base, name='base'),
]