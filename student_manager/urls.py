from django.urls import path, include

urlpatterns = [
    path('students/', include('student_manager.students.urls')),
    path('classrooms/', include('student_manager.classrooms.urls')),
    path('subjects/', include('student_manager.subjects.urls')),
    path('users/', include('student_manager.users.urls'))
]
