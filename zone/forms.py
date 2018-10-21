from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Images, Profile, Comments


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Images
        exclude = ['time', 'likes', 'tags', 'user_name', 'user_liked', 'location']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['date','first_name','last_name','email','user_name']
 
class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, help_text="Comment")
    class Meta:
        model = Comments
        fields = ('text',)
        exclude = ['image', 'time', 'user_name']




