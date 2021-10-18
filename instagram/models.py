from django.db import models

# Create your models here.

class Profile(models.Model):
    photo = models.ImageField()
    bio = models.CharField(max_length= 70)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

