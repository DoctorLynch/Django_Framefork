from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from shop.forms import ProductForm, VersionForm
from shop.models import Product, Category, Blogs, Version
from shop.services import get_cached_category_list


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'shop/category.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['categories'] = get_cached_category_list
        return context_data


@login_required
def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Категория - {category_item.name}'
    }
    return render(request, 'shop/products.html', context)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'shop/products.html'

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class BlogsListView(LoginRequiredMixin, ListView):
    model = Blogs
    template_name = 'shop/blogs.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publication_attribute=True)
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class BlogsCreateView(LoginRequiredMixin, CreateView):
    model = Blogs
    fields = '__all__'
    success_url = reverse_lazy('shop:list_blogs')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'shop.view_product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLE:
            key = f'version_list_{self.object.pk}'
            version_list = cache.get(key)
            if version_list is None:
                version_list = self.object.version_set.all()
                cache.set(key, version_list)
        else:
            version_list = self.object.version_set.all()

        context_data['versions'] = version_list
        return context_data


class BlogsDetailView(LoginRequiredMixin, DetailView):
    model = Blogs

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:list')

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFromset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFromset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFromset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class BlogsUpdateView(LoginRequiredMixin, UpdateView):
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


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('shop:list')


class BlogsDeleteView(LoginRequiredMixin, DeleteView):
    model = Blogs
    fields = '__all__'
    success_url = reverse_lazy('shop:list_blogs')


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version

    def form_valid(self, form):
        product_pk = self.kwargs['pk']  # Получаем pk продукта из URL
        product = Product.objects.get(pk=product_pk)  # Получаем объект продукта
        form.instance.product = product  # Устанавливаем продукт в поле версии
        return super().form_valid(form)
