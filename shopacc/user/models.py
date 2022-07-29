from django.db import models
from django.contrib.auth.models import User
from home.models import AccFifa
from django.utils.text import slugify 

# Create your models here.
class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   money = models.DecimalField(max_digits=10, decimal_places=3, default=0)

   def __str__(self):
       return self.user.username

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    number = models.IntegerField(default=0)
    product = models.ForeignKey(AccFifa, on_delete=models.CASCADE, blank= True, null= True)
    addCart = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username