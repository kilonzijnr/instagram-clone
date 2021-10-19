from django.db.models import fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Image, Profile

class UpdateProfileForm(ModelForm):
    """Method to define fields in profile form"""
    class Meta:
        model = Profile
        fields = ('user','username','bio','profile_photo')
        exclude = ['user']

class CreatePostForm(ModelForm):
    """Method to initialise a form for creating a new post"""
    
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ['likes','user']