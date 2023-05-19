from django import forms
from .models import *

class OcrUploadForm(forms.ModelForm):
    class Meta:
        model = Books        
        fields = ('file',)
        field_class = 'flex bg-orange-400 text-red-100 py-3'
        widgets = {
            'file': forms.FileInput(attrs={'class': field_class, 'placeholder': 'upload an image'}),
        }