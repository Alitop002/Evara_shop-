from django.contrib import admin
from shop.models import Category, Product

admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    models = Product
    exclude = ['discount_price',]
    list_display = ('name', 'price', 'discount',)
    list_display_links = ('name', 'price', 'discount',)


admin.site.register(Product, ProductAdmin)  