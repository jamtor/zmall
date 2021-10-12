from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ecommerce.api import views as qv

router = DefaultRouter()
router.register(r"category", qv.ProductCategoriesViewSet)
# router.register(r"products", qv.ProductDetailViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('category/image/<id>', qv.ImageCategoryAPIView.as_view()),
    path('<slug:slug>/image/<id>', qv.ImageProductAPIView.as_view()),
    path('<slug:slug>/product', qv.ProductAPIView.as_view(), name="product"),
    path('<slug:slug>/detail', qv.ProductDetailAPIView.as_view(), name="product-detail"),
]