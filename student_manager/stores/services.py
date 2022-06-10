from commons.exceptions import NotFoundException, ValidationException, ForbiddenException
from student_manager.users.models import User
from .models import CartItem, Product, Store, Cart
from django.db import transaction
from django.core.files import File

@transaction.atomic
def create_store(*, 
    user: User,
    image: File = None,
    name: str,
    url: str,
    email: str,
    address: str,
    city: str,
    province: str,
    landmark: str,
    longitude: int,
    latitude: int
) -> Store:
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

def add_item(*,
    cart: Cart,
    user: User = None,
    product: Product,
    quantity: int
) -> CartItem:
    cart_data = CartItem.objects.filter(cart=cart, product=product).first()

    if cart_data:
        cart_data.quantity += quantity
        cart_data.save()
    else:
        cart_data = CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity
        )

    return cart_data

def create_product(*,
    name: str,
    brand: str,
    description: str,
    average_cost: int,
    status: str,
    sellable: bool
) -> Product:
    product = Product.objects.create(
        name=name,
        brand=brand,
        description=description,
        average_cost=average_cost,
        status=status,
        sellable=sellable
    )
    return product

def delete_item(*,
    cart: Cart,
    user: User,
    product: Product
) -> CartItem:
    owner = cart.owner
    if user != owner:
        raise ForbiddenException()
    cart_item = CartItem.objects.filter(cart=cart, product=product).delete()
