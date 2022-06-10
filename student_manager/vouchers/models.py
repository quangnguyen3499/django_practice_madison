from django.db import models

class Voucher(models.Model):
    class VoucherType(models.TextChoices):
        CART_FIXED = "CART_FIXED", "Fixed Amount Discount Applied to Cart Total"
        CART_PERCENTAGE = "CART_PERCENTAGE", "Percentage Discount Applied to Cart Total"
        PRODUCT_FIXED = (
            "PRODUCT_FIXED",
            "Fixed Amount Discount Applied to Product Total",
        )
        PRODUCT_FIXED_PER_ITEM = (
            "PRODUCT_FIXED_PER_ITEM",
            "Fixed Amount Discount Applied to Product Per Item",
        )
        PRODUCT_PERCENTAGE = (
            "PRODUCT_PERCENTAGE",
            "Percentage Discount Applied to Product Total",
        )

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    user_limit = models.PositiveIntegerField(
        default=1,
    )
    max_redemption = models.PositiveIntegerField(
        default=0,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField(
        blank=True,
        null=True,
    )
    promo_type = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=VoucherType.choices,
    )
    discount_value = models.IntegerField()
    minimum_order_amount = models.IntegerField()
    min_order_count = models.IntegerField(default=0)
    max_order_count = models.IntegerField(default=0)
    exclusive_to_user = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    claimable = models.BooleanField(default=True)
