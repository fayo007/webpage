from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Form(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    is_checked = models.BooleanField(default=False)
    
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
     
    def __str__(self):
        return self.name
