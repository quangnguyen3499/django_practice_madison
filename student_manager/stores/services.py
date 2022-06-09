from commons.exceptions import NotFoundException
from student_manager.users.models import User
from .models import Store, Cart
from django.db import transaction

@transaction.atomic
def create_store(*, 
    user: User,
    image: str,
    name: str,
    url: str,
    email: str,
    address: str,
    city: str,
    province: str,
    landmark: str,
    longitude: int,
    latitude: int
):
    store = Store.objects.create(
        user=user,
        image=image,
        name=name,
        url=url,
        email=email,
        address=address,
        city=city,
        province=province,
        landmark=landmark,
        longitude=longitude,
        latitude=latitude
    )

    return store

def create_cart(*,
    owner: User,
    store: Store,
    ordering_for_id: int
):
    if ordering_for_id:
        try:
            user_check = User.objects.get(pk=ordering_for_id)
        except:
            raise NotFoundException({"message": "not found exception"})
    cart = Cart.objects.create(owner=owner,
        store=store,
        ordering_for=user_check
    )
    return cart

def update_cart(*,
    cart: Cart,
    ordering_for: User,
    owner: User
) -> Cart:
    cart.ordering_for = ordering_for
    cart.owner = owner
    cart.save()
    return cart
