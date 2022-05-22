from sys import breakpointhook
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)

class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True) 
    deleted_at = models.DateTimeField(max_length=(6), null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, max_length=(6))
    created_date = models.DateTimeField(auto_now_add=True, max_length=(6))
    
    objects = models.Manager()
    undeleted_objects = SoftDeleteManager()
    
    class Meta:
        db_table = "subject"

class ClassRoom(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True)
    deleted_at = models.DateTimeField(max_length=(6), null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, max_length=(6))
    created_date = models.DateTimeField(auto_now_add=True, max_length=(6))

    objects = models.Manager()
    undeleted_objects = SoftDeleteManager()
    
    class Meta:
        db_table = "class_room"

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    tel = models.CharField(max_length=20, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, null=True, blank=True)
    deleted_at = models.DateTimeField(max_length=(6), null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, max_length=(6))
    created_date = models.DateTimeField(auto_now_add=True, max_length=(6))
    subjects = models.ManyToManyField('Subject')

    objects = models.Manager()
    undeleted_objects = SoftDeleteManager()
    
    class Meta:
        db_table = "student"

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
    deleted_at = models.DateTimeField(max_length=(6), null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, max_length=(6))
    created_date = models.DateTimeField(auto_now_add=True, max_length=(6))
    
    objects = UserManager()
    undeleted_objects = SoftDeleteManager()

    USERNAME_FIELD = "username"
    
    class Meta:
        db_table = "auth_user"
