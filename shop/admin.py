from django.contrib import admin

from shop.models import Product, Blogs, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'description')


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'flag_of_version')
    list_filter = ('product',)
    search_fields = ('product',)
