from django.urls import path

from shop.apps import ShopConfig
from shop.views import contact, products

app_name = ShopConfig.name

urlpatterns = [
    path('', products, name='products'),
    path('contacts/', contact, name='contacts')
]