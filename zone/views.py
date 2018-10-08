# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# from templates import SignUpForm, NewPostForm, CommentForm, ProfileForm
# from django.contrib.auth.decorators import login_required
# from .models import Images, Profile, tags, Comments, Follow
# import datetime as dt
# from django.db import transaction
from django.shortcuts import render
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

# @login_required(login_url='/accounts/login/')
# def index(request):
#     user = request.user
#     images = Images.objects.filter(user_name=request.user)
#     profile = Profile.objects.filter(user_name=request.user)
#     avatar = Profile.profile_avatar
#     includes = {
#         "user":user,
#         "images":images,
#         "profile":profile,
#     }
#     return render(request,'ig/index.html', includes)