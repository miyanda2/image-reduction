import sys
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
# Create your models here.


class Upload(models.Model):
    name = models.CharField(max_length = 140,blank=False,null=True)
    uploadedImage =  models.ImageField(upload_to = 'Upload/',blank=False,null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.uploadedImage = self.compressImage(self.uploadedImage)
        super(Upload, self).save(*args, **kwargs)

    def compressImage(self,uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=35)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage
    

    # def get_absolute_url(self):
    #     return reverse("students_profile:student_profile_detail", args=[self.id])
    
    



# 