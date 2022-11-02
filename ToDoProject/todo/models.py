from django.db import models

# Create your models here.
class task(models.Model):
    heading = models.CharField(max_length=500)
    detail = models.CharField(max_length=100)
    date = models.DateField()
    is_deleted=models.CharField(max_length=2)
    image = models.ImageField(upload_to='images')  
