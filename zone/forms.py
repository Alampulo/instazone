# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Images, Profile, Comments

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=True,)
#     last_name = forms.CharField(max_length=30, required=True, )
#     email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name','last_name', 'email','password1','password2',)

# class NewPostForm(forms.ModelForm):
#     class Meta:
#         model = Images
#         exclude = ['time', 'likes', 'tags', 'user_name', 'user_liked']
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#             # 'location': forms.CheckboxSelectMultiple(),
#         }

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['date','first_name','last_name','email','user_name']
 
# class CommentForm(forms.ModelForm):
#     text = forms.CharField(max_length=1000, help_text="Comment")
#     class Meta:
#         model = Comments
#         fields = ('text',)
#         exclude = ['image', 'time', 'user_name']
