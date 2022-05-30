from django.contrib import admin
from users.models import User
from students.models import Student
from subjects.models import Subject
from classrooms.models import ClassRoom
from django.contrib.auth.models import Group

admin.site.register(Student)
admin.site.register(User)
admin.site.register(Subject)
admin.site.register(ClassRoom)
admin.site.unregister(Group)
