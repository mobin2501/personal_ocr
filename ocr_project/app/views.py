from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from . import forms

class HomeView(generic.TemplateView):
    template_name = 'home.html'
    

class OCRView(generic.FormView):
    template_name = 'ocr_image.html'
    form_class = forms.OcrUploadForm
    
    def form_valid(self, form):
        print('Form is valid')
        message = 'file is saved'
        
        print(message)
        form.save()
        return HttpResponse(message)
    
    def form_invalid(self,form):
        print('Form is invalid')
        print(form.errors)
        return HttpResponse(form.errors)
    
        

    

