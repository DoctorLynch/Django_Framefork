from django.shortcuts import render

from shop.models import Product


def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Товары'
    }
    return render(request, 'shop/products.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'shop/contacts.html', context)
