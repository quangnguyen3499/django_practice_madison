from django.urls import path
from .api import products, stores, carts

store_patterns = [
    path('', stores.CreateStoreAPIView.as_view(), name="create-store"),
    path('stores/list/', stores.ListStoreAPIView.as_view(), name="list-store"),
]

product_patterns = [
    path('products/list/', products.ListProductAPIView.as_view(), name="list-product"),
    path('products/', products.CreateProductAPIView.as_view(), name="create-product"),
]

carts_patterns = [
    path('carts/', carts.CreateCartAPIView.as_view(), name="create-cart"),
    path('carts/<int:id>/', carts.UpdateCartAPIView.as_view(), name="update-cart"),
    path('carts/<int:id>/items/', carts.AddCartItemAPIView.as_view(), name="add-item-to-cart"),
]

urlpatterns = (
    store_patterns + product_patterns + carts_patterns
)
