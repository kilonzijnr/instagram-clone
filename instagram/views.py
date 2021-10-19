from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from instagram.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import UpdateProfileForm,CreatePostForm

# Create your views here.

def homepage(request):
    """Method to render the HomePage"""
    if request.user.is_authenticated:
        users = Profile.get_following(request.user)
        posts = Image.get_images(users)
        alt_profiles = Profile.objects.all()

        return render(request,'insta/index.html',{"posts":posts,'profiles':alt_profiles})
    else:
        return redirect('login')