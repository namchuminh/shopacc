from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.text import slugify 


# Create your models here.

class AccFifa(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    sale = models.DecimalField(max_digits=10, decimal_places=3, default=50.000)
    image = models.ImageField(upload_to ='uploads/')
    image1 = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    image2 = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    image3 = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    timeUpload = models.DateTimeField(default=datetime.now, blank=True) 
    product = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    username = models.CharField(max_length=255, default="abc")
    password = models.CharField(max_length=255, default="xyz")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(AccFifa, self).save(*args, **kwargs)

    def __str__(self):
        return self.name




