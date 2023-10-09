from django.shortcuts import render

from shop.models import Product


def base(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Товары'
    }
    return render(request, 'shop/base.html', context)
