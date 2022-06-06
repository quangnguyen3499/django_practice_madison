# from django.db import models
# from django.utils import timezone

# from commons.exceptions import ValidationException

# class Cart(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     owner = models.ForeignKey(
#         "users.User",
#         related_name="carts",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )
#     ordering_for = models.ForeignKey(
#         "users.CommunityLeaderSuki",
#         related_name="+",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )
#     store = models.ForeignKey(
#         Store, related_name="carts", on_delete=models.CASCADE, null=True
#     )
#     updated_at = models.DateTimeField(auto_now_add=timezone.now())
#     created_at = models.DateTimeField(auto_now=timezone.now())
    
# class Store(models.Model):
#     user = models.ForeignKey(
#         "users.User", related_name="stores", on_delete=models.PROTECT
#     )
#     image = models.ImageField(upload_to=store_img_path, null=True, blank=True)
#     name = models.CharField(max_length=255)
#     url = models.CharField(max_length=255, unique=True, db_index=True)
#     email = models.CharField(max_length=255, null=True, blank=True)
#     address = models.CharField(max_length=255)
#     barangay = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     province = models.CharField(max_length=255)
#     landmark = models.TextField()
#     latitude = models.DecimalField(
#         max_digits=11, decimal_places=8, null=True, blank=True
#     )
#     longitude = models.DecimalField(
#         max_digits=11, decimal_places=8, null=True, blank=True
#     )
#     active = models.BooleanField(default=True)
#     updated_at = models.DateTimeField(auto_now_add=timezone.now())
#     created_at = models.DateTimeField(auto_now=timezone.now())

#     def __str__(self):
#         return self.url
   
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     brand = models.CharField(max_length=255, null=True, blank=True)
#     description = models.TextField(default="", blank=True)
#     average_cost = models.DecimalField(max_digits=19, decimal_places=4, default=0)
#     status = models.CharField(max_length=20, null=True, db_index=True, blank=True)
#     sellable = models.BooleanField(default=False)
#     updated_at = models.DateTimeField(auto_now_add=timezone.now())
#     created_at = models.DateTimeField(auto_now=timezone.now())

#     def __str__(self):
#         return f"{self.sku} - {self.name}"
    
# class Order(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     order_number = models.CharField(
#         max_length=32, default=generate_order_id, db_index=True
#     )
#     store = models.ForeignKey(
#         Store, related_name="orders", on_delete=models.SET_NULL, null=True, blank=True
#     )
#     user = models.ForeignKey(
#         "users.User",
#         related_name="orders",
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#     )
#     cart = models.ForeignKey(
#         Cart, related_name="orders", on_delete=models.SET_NULL, null=True, blank=True
#     )
#     batch = models.ForeignKey(
#         CutoffBatch,
#         related_name="orders",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         db_index=True,
#     )
#     sale = models.ForeignKey(
#         "inventory.Sale",
#         related_name="orders",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )
#     delivery_method = models.CharField(
#         max_length=32,
#         choices=DeliveryMethod.choices,
#         null=True,
#         blank=True,
#         db_index=True,
#     )
#     store_address = models.ForeignKey(
#         StoreAddress, related_name="+", on_delete=models.SET_NULL, null=True
#     )
#     delivery_address = models.ForeignKey(
#         DeliveryAddress, related_name="+", on_delete=models.SET_NULL, null=True
#     )
#     payment_status = models.CharField(
#         max_length=20,
#         choices=PaymentStatus.choices,
#         default=PaymentStatus.TO_COLLECT,
#         db_index=True,
#     )
#     status = models.CharField(
#         max_length=20,
#         choices=OrderStatus.choices,
#         default=OrderStatus.PENDING,
#         db_index=True,
#     )
#     total_discount_amount = PriceField(default=0)
#     total_items_amount = PriceField(default=0)
#     total_amount = PriceField(default=0)
    
#     estimated_delivery_date = models.DateField(null=True, blank=True, db_index=True)
#     approved_at = models.DateTimeField(null=True, blank=True, db_index=True)
#     canceled_at = models.DateTimeField(null=True, blank=True, db_index=True)
#     received_at = models.DateTimeField(null=True, blank=True, db_index=True)
    
#     updated_at = models.DateTimeField(auto_now_add=timezone.now())
#     created_at = models.DateTimeField(auto_now=timezone.now())
   