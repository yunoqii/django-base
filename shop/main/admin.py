from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price',  'available', 'created', 'updated')
    list_filter = ('category', 'available', 'created', 'updated')
    list_editable = ('available', 'price')
    prepopulated_fields = {'slug': ('name',)}
