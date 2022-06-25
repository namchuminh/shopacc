from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class AccFifa(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    sale = models.DecimalField(max_digits=10, decimal_places=3, default=50.000)
    image = models.ImageField(upload_to ='uploads/')
    timeUpload = models.DateTimeField(default=datetime.now, blank=True) 
    product = models.BooleanField(default=True)

    def __str__(self):
        return self.name




