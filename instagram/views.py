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

def user_profile(request,pk):
    """Method to manage the User Profile"""
    user = User.objects.get(pk=pk)
    try:
        profile = Profile.objects.get(user=user)
        followers = profile.total_followers()
        posts = Image.objects.filter(user = user)
        return render(request,'insta/profile.html',{"profile":profile,"posts":posts,"followers":followers})

    except Exception as e:
        print(e)
        messages.success(request,'Kindly set up your profile!')
        return redirect('update_profile')

def update_profile(request):
    """Method to handle data update in User Profile"""
    
