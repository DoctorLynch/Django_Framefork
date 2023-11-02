from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from shop.forms import ProductForm, VersionForm
from shop.models import Product, Category, Blogs, Version


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
        'object_list': Product.objects.filter(category_id=pk, owner=request.user),
        'title': f'Категория - {category_item.name}'
    }
    return render(request, 'shop/products.html', context)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('shop:list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        
        return super().form_valid(form)


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
    form_class = ProductForm
    success_url = reverse_lazy('shop:list')

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


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version

    def form_valid(self, form):
        product_pk = self.kwargs['pk']  # Получаем pk продукта из URL
        product = Product.objects.get(pk=product_pk)  # Получаем объект продукта
        form.instance.product = product  # Устанавливаем продукт в поле версии
        return super().form_valid(form)


