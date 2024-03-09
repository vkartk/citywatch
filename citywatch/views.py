from django.shortcuts import render
from django.contrib import messages

from .forms import IssueForm

def home(request):
    return render(request, 'pages/home.html')

def map(request):
    return render(request, 'pages/map.html')

def reports(request):
    return render(request, 'pages/reports.html')

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
