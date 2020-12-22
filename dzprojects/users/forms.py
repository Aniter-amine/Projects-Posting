from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Prof
from django import forms
from PIL import Image
# Categories settings


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password1'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password2'}),
        }


class ProfForm(ModelForm):
    class Meta:
        model = Prof
        fields = ['image', 'nickname', 'work', 'phone', 'linkedin_link', 'instagram_link',
                  'facebook_link', 'youtube_link', 'twitter_link', 'bio']

        widgets = {
            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname'}),
            'work': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Work'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'linkedin_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Linkedin'}),
            'instagram_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Instagram'}),
            'facebook_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Facebook'}),
            'youtube_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Youtube'}),
            'twitter_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Twitter'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio'}),
        }
