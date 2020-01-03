from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Upload
from .forms import ImageUploadForm
from django.views.generic import CreateView, TemplateView,DetailView
from django.urls import reverse_lazy, reverse
# Create your views here.


class ImageUploadView(CreateView):
    model = Upload
    form_class = ImageUploadForm
    template_name  ="compression/upload.html"
    # success_url = reverse_lazy('uploaded')

    def get_success_url(self):
        return reverse('image_detail', args=[self.object.id])


class ImageDetailView(DetailView):
    model = Upload
    context_object_name = 'image'
    template_name = 'compression/image.html'

class UploadedView(TemplateView):
    template_name="compression/uploaded.html"

