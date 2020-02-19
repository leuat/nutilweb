from django.db import models
from django.forms import ModelForm

# Create your models here.
class UploadFile(models.Model):
	name = models.CharField(max_length=100)
	file = models.FileField(upload_to='uploads/')


