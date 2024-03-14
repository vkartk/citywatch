from .models import Issue
from django.contrib.auth import authenticate, login

def associate_user_issues(email, user):
                issues = Issue.objects.filter(user__isnull=True, email=email)
                issues.update(user=user)

def handle_SignIn(request, userData):

    user = authenticate(username=userData['username'], password=userData['password'])
    if user is not None:
        login(request, user)
