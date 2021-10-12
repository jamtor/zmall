from django.db import models
from rest_framework import serializers
from ecommerce.models import ProductCategories, Product

class ProductCategoriesSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = ProductCategories
        exclude = ["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d %Y")
    

    def get_photo(self, instance):
        request = self.context.get('request')
        photo = "image/" + str(instance.id)
        return request.build_absolute_uri(photo)

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(read_only=True)
    seller = serializers.StringRelatedField(read_only=True)
    photo = serializers.SerializerMethodField('get_photo')
    created_at = serializers.SerializerMethodField()
    category_slug = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Product
        exclude = ["category", "updated_at"]

    def get_category_slug(self, instance):
        return instance.category.slug

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d %Y")

    # def get_photo(self, instance):
    #     return instance.photo.url
    
    def get_photo(self, instance):
        request = self.context.get('request')
        photo = "image/" + str(instance.id)
        return request.build_absolute_uri(photo)
    
    
   