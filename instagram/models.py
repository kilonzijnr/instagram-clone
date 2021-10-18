from django.db import models

# Create your models here.

class Profile(models.Model):
    """Model for handling User Profile"""

    photo = models.ImageField()
    bio = models.CharField(max_length= 70)

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Likes(models.Model):
    """Model for handling Image likes"""

    likes = models.IntegerField(default=0)




