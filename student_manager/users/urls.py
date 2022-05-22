from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.CreateUserView.as_view(), name='create-user'),
    path('list', views.ListUserView.as_view(), name='get-list-user'),
    path('<int:user_id>', views.GetAndUpdateAndDeleteUserView.as_view(), name='get-update-delete-user'),
    # path('about/', TemplateView.as_view(template_name="about.html"))
]
