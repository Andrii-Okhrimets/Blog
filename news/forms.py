from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLogup(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'special', 'size': '35'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'special', 'size': '36'}))

class UserLogin(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'special', 'size': '35'}))
    email = forms.EmailField(label='email', widget=forms.EmailInput(attrs={'class': 'special', 'size': '40'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'special', 'size': '36'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'special', 'size': '23'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        
