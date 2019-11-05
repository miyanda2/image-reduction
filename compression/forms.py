from django import forms
from .models import Upload


class ImageUploadForm(forms.ModelForm):


    class Meta:
        model = Upload
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)        
        self.fields['name'].widget.attrs.update({'class':'form-control',"placeholder":'Enter Name Of Image', 'id':'name'})
        self.fields['uploadedImage'].widget.attrs.update({'class':'form-control', "placeholder":"Upload", 'id':'uploadedImage'})
