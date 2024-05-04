from django.urls import path
from .views import ProductList, AllProductList, detail, product_by_category, rate
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductList.as_view(), name='index'),
    path('products/', AllProductList.as_view(), name='all_products'),
    path('product/<int:product_id>/', detail, name='detail'),
    path('product-by/<int:pk>/', product_by_category, name="product_by_category"),
    path('rate/<int:post_id>/<int:rating>/', rate),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
