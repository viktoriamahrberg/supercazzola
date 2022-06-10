from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Product details to display in admin panel
    """
    list_display = (
        'name',
        'country',
        'category',
        'alc',
        'image',
        'price',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category details to desplay in admin panel
    """
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
