from django.db import models
from django.conf import settings

class ProductCategories(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to = 'categories_pics',blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Seller(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = 'seller_pics',blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    photo = models.ImageField(upload_to = 'product_pics')
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE,related_name="product")
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




