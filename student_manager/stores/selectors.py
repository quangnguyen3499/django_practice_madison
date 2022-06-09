from commons.exceptions import NotFoundException, ValidationException
from .models import Store, Product, Cart
from django.db.models.query import QuerySet
from django.db.models import Q

def get_list_store(*, name: str) -> QuerySet[Store]:
    stores = Store.objects.filter(Q(name__iexact=name))
    return stores

def get_store_by_url(*, url: str) -> Store:
    store = Store.objects.filter(url=url).first()
    return store

"""Get all available products for a store and filter out non sellable"""
def list_product(*, filter=None) -> QuerySet[Store]:
    products = Product.objects.prefetch_related(
        "store_configs"
        ).filter(
            **filter,
            sellable=True,
    )
    return products

def get_store_by_id(*, pk: int) -> Store:
    store = Store.objects.filter(pk=pk).first()
    if not store:
        raise ValidationException({"message": "object not found"})
    return store

def get_cart_by_id(*,
    pk: int
) -> Cart:
    try:
        cart = Cart.objects.get(pk=pk)
    except:
        raise NotFoundException()
    return cart
