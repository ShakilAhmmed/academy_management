from django.contrib.auth.forms import AuthenticationForm
from django import forms


class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-lg '}))
