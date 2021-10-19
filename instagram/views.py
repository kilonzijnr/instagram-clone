from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from instagram.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

