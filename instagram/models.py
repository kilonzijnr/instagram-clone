from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """Model for handling User Profile"""

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    username = models.CharField(max_length = 25)
    signup_date = models.DateTimeField(auto_now_add= True)
    profile_photo = models.ImageField()
    followers = models.ManyToManyField(User, related_name='followers', blank= True)
    bio = models.CharField(max_length= 70)

    def __str__(self):
        return self.name

    def total_followers(self):
        """Method to return total numberof followers"""
        return self.followers.count()

    def save_profile(self):
        """Method to save profile to the database"""
        self.save()

    def delete_profile(self):
        """Method to delete profile from the database"""
        self.delete()

    def update_profile(self,new):
        """Method to update user profile
        
        Args:
            new([type]): [description]

        """
        self.username = new.username
        self.bio = new.bio
        self.profile_photo = new.profile_pic
        self.save()

    @classmethod 
    def get_following(cls,user):
        """Method to return all users a specific user is following """
        following = user.followers.all()
        users = []
        for profile in following:
            user = User.objects.get(profile = profile)
            users.append(user)

        return users

    @classmethod 
    def search_profile(cls,search_term):
        """Method to return profiles with a provided search term
        
        Args:
            search_term([type]): [description]

        Returns:
            [type]: [description]
        """
        profiles = cls.objects.filter(username_icontains = search_term)

        return profiles




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
    
    

