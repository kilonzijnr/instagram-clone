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
    if request.method == 'POST':
        form =  UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_bound():
            form.save()
            return redirect('profile',request.user.pk)
        else:
            messages.success(request,'We are having prblems with your profile form')
            return render(request,'insta/update_profile.html',{"form":form})

    else:
        form = UpdateProfileForm(instance=request.user.profile)
        return render(request,'insta/update.html',{"form":form})


def post(request,user):
    """Method to handle new post"""
    post = Image(user == request.user)
    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'You have succesfully created your post!')
        return redirect('home')
    else:
        form = CreatePostForm(instance=post)
        return render(request,'insta/add_post.html',{'form':form})


def search_profile(request):
    """Method that will display search results"""
    if 'search_term' in request.GET and request.GET['search_term']:
        try:
            search_term = request.GET['search_term']
            profiles = Profile.search_profile(search_term)
            return render(request,"insta/search.html",{'profiles':profiles,"term":search_term})
        except Exception as e:
            print(e)
            
    else:
        messages.success(request,"Kindly make an input to complete your search!")
        return HttpResponseRedirect(reverse('home'))