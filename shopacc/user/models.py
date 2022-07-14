from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   money = models.DecimalField(max_digits=10, decimal_places=3, default=0)

   def __str__(self):
       return self.user.username