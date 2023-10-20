from django.contrib import admin

from shop.models import Category, Product, Blogs, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description')


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product',)
    list_filter = ('product',)
    search_fields = ('product',)
