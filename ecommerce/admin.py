from django.contrib import admin
from ecommerce.models import ProductCategories, Seller, Product

# Register your models here.
admin.site.register(ProductCategories)
admin.site.register(Seller)
admin.site.register(Product)