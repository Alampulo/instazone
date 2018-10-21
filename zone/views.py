from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignupForm, NewPostForm, CommentForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Images, Profile,Comments
import datetime as dt
from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('home')

        return HttpResponse('yo niccur Thank you for your email confirmation. <a href="/accounts/login">Click</a>to login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    images = Images.objects.all()
    profile = Profile.objects.filter(user_name=request.user)
    # avatar = Profile.profile_avatar
    includes = {
        "user":user,
        "images":images,
        "profile":profile,
    }
    return render(request,'ig/index.html',{"images": images})
    
def new_post(request):
   current_user = request.user
   if request.method == 'POST':
       form =NewPostForm(request.POST,request.FILES)
       if form.is_valid():
           image = form.save(commit=False)
           image.user = current_user
           image.save()
       return render(request, 'new_post.html', {"form": form})

   else:
       form = NewPostForm()
   return render(request, 'new_post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def explore(request):
    date= dt.date.today
    image = Images.objects.all()
    return render(request, 'ig/explore.html', {"date":date, "image":image})

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    user = request.user
    form= ProfileForm()
    images = Images.objects.filter(user_name=request.user)
    profile = Profile.objects.filter(user_name=request.user)
    avatar = Profile.profile_avatar
    includes = {
        "user":user,
        "images":images,
        "profile":profile,
        "avatar": avatar,
        "form": form,
    }
    return render(request, 'ig/profile.html', includes)

@transaction.atomic
@login_required(login_url='/accounts/login')
def change_profile(request, user_id):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            current_user = request.user
            form.save(commit=False)
            profile.user =request.user
            profile.save()
            return redirect('profile', user_id)
    
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit-profile.html', {"form": form})

def search_profile(request):
    if 'user_name' in request.GET and request.GET["user_name"]:
        search_term = request.GET.get("user_name")
        searched_profiles = Profile.search_profile(image)
        images = Images.objects.all()
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"
        return render(request, 'ig/search.html', {"message":message, "searched_profiles": searched_profiles, 'user':user, "images":images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'ig/search.html', {"message": message})

def comment(request):
    current_user = request.user
    image = Image.objects.get()
    comment = Comments.objects.all()
    profile = Profile.objects.filter(user_name_id = current_user)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            profile.user = current_user
            comment.save()
            return redirect('explore')
    
    else:
        form = CommentForm()
    return render(request, 'ig/comment.html', {"form":form, 'image': image, "comment":comment,})