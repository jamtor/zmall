from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from ecommerce.models import ProductCategories, Product

@receiver(pre_save, sender=ProductCategories)
def add_slug_to_categories(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string

@receiver(pre_save, sender=Product)
def add_slug_to_product(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.name)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string
