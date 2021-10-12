from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.api.serializers import ProductCategoriesSerializer, ProductSerializer
from ecommerce.api.permissions import IsAuthorOrReadOnly
from ecommerce.api.custom import JPEGRenderer
from ecommerce.models import ProductCategories, Product

class ProductCategoriesViewSet(viewsets.ModelViewSet):
    queryset = ProductCategories.objects.all()
    lookup_field = "slug"
    serializer_class = ProductCategoriesSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# class ProductDetailViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     lookup_field = "slug"
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

class ProductAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        kwarg_id = self.kwargs.get("slug")
        return Product.objects.filter(category__slug = kwarg_id)

class ProductDetailAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        kwarg_id = self.kwargs.get("slug")
        return Product.objects.filter(slug = kwarg_id)


class ImageCategoryAPIView(generics.RetrieveAPIView):

    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        queryset = ProductCategories.objects.get(id=self.kwargs['id']).photo
        data = queryset
        return Response(data, content_type = 'image/jpg')

class ImageProductAPIView(generics.RetrieveAPIView):

    renderer_classes = [JPEGRenderer]

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.get(id=self.kwargs['id']).photo
        data = queryset
        print(data)
        return Response(data, content_type = 'image/jpg')