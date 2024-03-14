from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, QueryDict


import json
from .models import Issue, IssueCategory
from .forms import IssueForm, SignUpForm, SignInForm
from .utils import handle_SignIn, associate_user_issues

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
            issue = form.save(commit=False)
            if request.user.is_authenticated:
                issue.user = request.user
            issue.save()
            messages.success(request, "Issue reported successfully!")
            return redirect('IssuePage', id=issue.id)
        else:
            messages.error(request, "Issue report failed!")
    else:
        form = IssueForm()

    return render(request, "pages/report.html", {"form": form})

def SignUp(request):

    if request.user.is_authenticated:
        return redirect('Dashboard')
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully!")

            userData = {
                'username' : form.cleaned_data['username'],
                'password' : form.cleaned_data['password1'],
            }

            handle_SignIn(request, userData)
            associate_user_issues(form.cleaned_data['email'], user)

            return redirect('Dashboard')

        else:
            messages.error(request, "Account creation failed!")

    else:
        form = SignUpForm()

    return render(request, "pages/auth/signup.html", {"form": form})

def SignIn(request):

    if request.user.is_authenticated:
        return redirect('Dashboard')
    
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            userData = {
                'username' : form.cleaned_data['username'],
                'password' : form.cleaned_data['password'],
            }

            handle_SignIn(request, userData)

            associate_user_issues(request.user.email , request.user)

            return redirect('Dashboard')
        
        else:
            messages.error(request, "Sign in failed!")

    else:
        form = SignInForm()

    return render(request, "pages/auth/signin.html", {"form": form})

def SignOut(request):
    logout(request)
    return redirect('home')

def Dashboard(request):

    if not request.user.is_authenticated:
        return redirect('signin')

    issues = Issue.objects.filter(user=request.user).order_by('-created_at')
    categories = IssueCategory.objects.all()

    return render(request, "pages/dashboard.html", {"issues": issues, "categories": categories})

def IssuePage(request, id):

    issue = Issue.objects.get(id=id)

    return render(request, "pages/issue.html", {"issue": issue})


def StaffDashboard(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('signin')
    
    issues = Issue.objects.all().order_by('-created_at')
    categories = IssueCategory.objects.all()
    users = User.objects.all()
    statusCounts = {}
    for statusKey, statusLabel in Issue.STATUS_CHOICES:
        statusCounts[statusLabel] = Issue.objects.filter(status=statusKey).count()

    context = {
        "issues": issues,
        "categories": categories,
        "statusCounts": statusCounts,
        "users": users,
    }

    return render(request, "pages/staff_dashboard.html", context)


def IssueAPI(request, id=None):

    if request.method == "GET":
        if id:
            issue = Issue.objects.get(id=id)
            return JsonResponse(issue.to_dict())
        else:
            issues = Issue.objects.all()
            return JsonResponse([issue.to_dict() for issue in issues], safe=False)
        
    if not request.user.is_authenticated or not request.user.is_staff:
            return JsonResponse({"message": "Unauthorized"}, status=401)
        
    if request.method == 'PUT':
        issue = Issue.objects.get(id=id)
        raw_data = request.body
        data = json.loads(raw_data.decode())
        print(data)
 
        issue.status = data['status'] if 'status' in data else issue.status
        issue.save()
        return JsonResponse(issue.to_dict())
                

    
    if request.method == "DELETE":
        issue = Issue.objects.get(id=id)
        issue.delete()
        return JsonResponse({"message": "Issue deleted successfully!"})
   

def CategoryAPI(request, id=None):
    if id:
        category = IssueCategory.objects.get(id=id)
        issuesInCategory = Issue.objects.filter(category=category)
        category = category.to_dict()
        category['issueCount'] = issuesInCategory.count()

        for statusKey, statusLabel in Issue.STATUS_CHOICES:
            category[statusLabel] = issuesInCategory.filter(status=statusKey).count()

        return JsonResponse(category)
    else:
        categories = IssueCategory.objects.all()
        categoryList = []
        for category in categories:
            issuesInCategory = Issue.objects.filter(category=category)
            category = category.to_dict()
            category['issueCount'] = issuesInCategory.count()

            for statusKey, statusLabel in Issue.STATUS_CHOICES:
                category[statusLabel] = issuesInCategory.filter(status=statusKey).count()

            categoryList.append(category)
        return JsonResponse(categoryList, safe=False)