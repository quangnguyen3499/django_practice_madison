from django.urls import path
from . import views

urlpatterns = [
    path('', views.save_file, name="upload-file-to-s3"),
    path('file/', views.UploadFile.as_view(), name="upload-file"),
]
