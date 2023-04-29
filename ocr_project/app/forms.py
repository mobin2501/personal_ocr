from django.forms import forms,ModelForm
from .models import *

class OcrUploadForm(ModelForm):
    class Meta:
        model = Books        
        fields = ('file',)