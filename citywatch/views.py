from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Issue, IssueCategory
from .forms import IssueForm, SignUpForm, SignInForm

def home(request):
    issues = Issue.objects.all().order_by('-created_at')
    return render(request, 'pages/home.html', {"issues": issues})

def map(request):
    return render(request, 'pages/map.html')

def reports(request):
    issues = Issue.objects.all().order_by('-created_at')
    return render(request, 'pages/reports.html', {"issues": issues})

def report(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Issue reported successfully!")
        else:
            messages.error(request, "Issue report failed!")
    else:
        form = IssueForm()

    return render(request, "pages/report.html", {"form": form})

def SignUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")

            userData = {
                'username' : form.cleaned_data['username'],
                'password' : form.cleaned_data['password1'],
            }

            return handle_SignIn(request, userData)

        else:
            messages.error(request, "Account creation failed!")

    else:
        form = SignUpForm()

    return render(request, "pages/auth/signup.html", {"form": form})

def SignIn(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            userData = {
                'username' : form.cleaned_data['username'],
                'password' : form.cleaned_data['password'],
            }

            handle_SignIn(request, userData)
        else:
            messages.error(request, "Sign in failed!")

    else:
        form = SignInForm()

    return render(request, "pages/auth/signin.html", {"form": form})

def SignOut(request):
    logout(request)
    return redirect('home')

def Dashboard(request):

    issues = Issue.objects.all().order_by('-created_at')
    categories = IssueCategory.objects.all()

    return render(request, "pages/dashboard.html", {"issues": issues, "categories": categories})

def IssuePage(request, id):

    issue = Issue.objects.get(id=id)

    return render(request, "pages/issue.html", {"issue": issue})

def handle_SignIn(request, userData):

    user = authenticate(username=userData['username'], password=userData['password'])
    if user is not None:
        login(request, user)
        messages.success(request, "Sign in successful!")

        return redirect('Dashboard')