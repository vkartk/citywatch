from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'
        wdigets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
        exclude = ['created_at', 'updated_at', 'status',]