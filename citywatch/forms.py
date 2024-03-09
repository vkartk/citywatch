from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = '__all__'
        exclude = ['created_at', 'updated_at']