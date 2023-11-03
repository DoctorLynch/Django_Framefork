from django.urls import path

from shop.apps import ShopConfig
from shop.views import ProductListView, ProductCreateView, ProductDetailView, \
    ProductUpdateView, ProductDeleteView, BlogsListView, BlogsDetailView, BlogsUpdateView, BlogsDeleteView, \
    BlogsCreateView

app_name = ShopConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('create_blogs/', BlogsCreateView.as_view(), name='create_blogs'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('blogs/', BlogsListView.as_view(), name='list_blogs'),
    path('view_blogs/<int:pk>/', BlogsDetailView.as_view(), name='view_blogs'),
    path('edit_blogs/<int:pk>/', BlogsUpdateView.as_view(), name='edit_blogs'),
    path('delete_blogs/<int:pk>/', BlogsDeleteView.as_view(), name='delete_blogs'),

]
