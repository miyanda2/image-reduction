from django.shortcuts import render
from .models import Upload
from .forms import ImageUploadForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
# Create your views here.


class ImageUploadView(CreateView):
    model = Upload
    form_class = ImageUploadForm
    template_name  ="compression/upload.html"
    success_url = reverse_lazy('uploaded')


class UploadedView(TemplateView):
    template_name="compression/uploaded.html"