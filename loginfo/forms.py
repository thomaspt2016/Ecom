from django import forms
from django.contrib.auth.models import User
# class SignupForm(forms.ModelForm):#signuoform definition

#     class Meta:
#         model=User#alreeady defined inside django.contrib.auth.models
#         fields=['username','password','email','first_name','last_name']
from loginfo.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','password1','password2','email','first_name','last_name','phone']

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)