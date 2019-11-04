from django.urls import path
from  . import views


urlpatterns = [
    path('', views.ImageUploadView.as_view(), name="upload_image"),
    path('uploaded/', views.UploadedView.as_view(),name="uploaded")
]
