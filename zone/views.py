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
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. <a href="/accounts/login">Click</a>to login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    images = Images.objects.all()
    # profile = Profile.objects.filter(user_name=request.user)
    # avatar = Profile.profile_avatar
    # includes = {
    #     "user":user,
    #     "images":images,
    #     "profile":profile,
    # }
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