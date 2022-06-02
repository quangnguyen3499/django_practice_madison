from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets
 
admin.site.register(User, UserAdmin)
