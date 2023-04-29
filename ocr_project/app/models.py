from django.db import models

class Books(models.Model):
    file = models.FileField(upload_to='books/')
