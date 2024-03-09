from django import forms
from django.forms.widgets import HiddenInput
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