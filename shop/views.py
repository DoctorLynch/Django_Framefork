from django.shortcuts import render

from shop.models import Product, Category


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Товары'
    }
    return render(request, 'shop/products.html', context)


def category(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Категории'
    }
    return render(request, 'shop/category.html', context)


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Категория - {category_item.name}'
    }
    return render(request, 'shop/products.html', context)
