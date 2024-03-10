from django import forms
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'
        widgets = {
            'latitude': HiddenInput(),  
            'longitude': HiddenInput(),
        }
        exclude = ['created_at', 'updated_at', 'status',]

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())