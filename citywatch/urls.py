from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('reports/', views.reports, name='reports'),
    path('report/', views.report, name='report'),
]