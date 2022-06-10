from django.urls import path
from . import views

urlpatterns = [
    path('vouchers/', views.CreateVoucherAPIView.as_view(), name="create-voucher"),
]
