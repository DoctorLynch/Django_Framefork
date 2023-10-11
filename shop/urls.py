from django.urls import path

from shop.apps import ShopConfig
from shop.views import category, products, category_products

app_name = ShopConfig.name

urlpatterns = [
    path('', products, name='products'),
    path('category/', category, name='category'),
    path('<int:pk>/products/', category_products, name='category_products')

]