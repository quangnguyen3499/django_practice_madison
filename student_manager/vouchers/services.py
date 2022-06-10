from .models import Voucher

def create_voucher(*,
    name: str,
    code: str,
    user_limit: int,
    max_redemption: int,
    valid_until: DateTime
    promo_type: str,
    discount_value: int,
    minimum_order_amount: int,
    min_order_count: int,
    max_order_count: int,
    exclusive_to_user: bool,
    active: bool,
    claimable: bool
) -> Voucher:
    