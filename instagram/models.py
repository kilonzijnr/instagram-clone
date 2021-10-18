from django.db import models

# Create your models here.

class Profile(models.Model):
    photo = models.ImageField()
    bio = models.CharField(max_length= 70)

