from django.urls import path

from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('img/',views.OCRView.as_view(), name='ocr_image')
]
