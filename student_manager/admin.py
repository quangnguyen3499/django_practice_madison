from django.contrib import admin
from .models import User, Student, Subject, ClassRoom
from django.contrib.auth.models import Group

admin.site.register(Student)
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.unregister(Group)
