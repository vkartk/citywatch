from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def map(request):
    return render(request, 'pages/map.html')

def reports(request):
    return render(request, 'pages/reports.html')

def report(request):
    return render(request, 'pages/report.html')