from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def map(request):
    return render(request, 'map.html')

def reports(request):
    return render(request, 'reports.html')

def report(request):
    return render(request, 'report.html')