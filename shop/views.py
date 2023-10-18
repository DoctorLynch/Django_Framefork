from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from shop.models import Product, Category, Blogs


class ProductListView(ListView):
    model = Product
    template_name = 'shop/products.html'


class BlogsListView(ListView):
    model = Blogs
    template_name = 'shop/blogs.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_attribute=True)
        return queryset


class CategoryListView(ListView):
    model = Category
    template_name = 'shop/category.html'


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Категория - {category_item.name}'
    }
    return render(request, 'shop/products.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('shop:list')


class BlogsCreateView(CreateView):
    model = Blogs
    fields = '__all__'
    success_url = reverse_lazy('shop:list_blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


class BlogsDetailView(DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('shop:list')


class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = '__all__'

    # success_url = reverse_lazy('shop:list_blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('shop:view_blogs', args=[self.kwargs.get('pk')])



class ProductDeleteView(DeleteView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('shop:list')


class BlogsDeleteView(DeleteView):
    model = Blogs
    fields = '__all__'
    success_url = reverse_lazy('shop:list_blogs')
