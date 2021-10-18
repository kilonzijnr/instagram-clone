from django.db import models
from django.db.models.deletion import CASCADE

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

class Image(models.Model):
    """Model for handling Image posts by users"""

    image = models.ImageField()
    name = models.CharField(max_length= 25)
    caption = models.CharField(max_length= 100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default= None)
    likes = models.ForeignKey(Likes, on_delete=CASCADE, default=None)
    comments = models.CharField(max_length= 120)
    post_time = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-post_time']

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    

