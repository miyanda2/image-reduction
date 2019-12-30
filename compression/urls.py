from django.urls import path
from  . import views


urlpatterns = [
    path('', views.ImageUploadView.as_view(), name="upload_image"),
    path('<int:pk>/image/', views.ImageDetailView.as_view(), name='image_detail'),
    path('uploaded/', views.UploadedView.as_view(),name="uploaded")
]
