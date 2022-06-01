from django.urls import path
from student_manager.users.serializers import UserRegisterSerializer
from . import views

urlpatterns = [
    # path('', auth_register_views.RegisterView.as_view(
    #     serializer_class=UserRegisterSerializer
    # ), name='create-user'),
    path('', views.CreateUserView.as_view(), name='create-user'),
    path('list', views.ListUserView.as_view(), name='get-list-user'),
    path('<int:user_id>', views.GetAndUpdateAndDeleteUserView.as_view(), name='get-update-delete-user'),
    path('reset_mail/', views.SendMailResetPasswordView.as_view(), name="send-mail-reset-password"),
    path('send_otp/', views.SendResetOtp.as_view(), name="send-otp"),
    path('send_token/', views.PasswordOTPView.as_view(), name="send-token-reset"),
    path('change_password/', views.ChangePasswordView.as_view(), name="change-password"),
]
