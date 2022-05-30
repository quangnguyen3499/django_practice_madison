from datetime import timedelta
import secrets
import string
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

def generate_otp():
    return "".join(secrets.choice(string.digits) for i in range(6))

class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            is_superuser = False,
            is_staff = False
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, first_name=None, last_name=None, password=None):
        user = self.create_user(email,
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(max_length=(6), null=True, blank=True)
    otp_code = models.CharField(max_length=6, default=generate_otp)
    otp_expires_at = models.DateTimeField(default=timezone.now)
    old_hash = models.CharField(max_length=255, null=True, blank=True)
    deleted_at = models.DateTimeField(max_length=(6), null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, max_length=(6))
    created_date = models.DateTimeField(auto_now_add=True, max_length=(6))

    objects = UserManager()

    USERNAME_FIELD = "username"

    def generate_otp(self):
        self.otp_code = generate_otp()
        self.otp_expires_at = timezone.now() + timedelta(hours=24)
        self.save()
