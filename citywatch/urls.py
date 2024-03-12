from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('reports/', views.reports, name='reports'),
    path('report/', views.report, name='report'),

    path('signin/', views.SignIn, name='signin'),
    path('signup/', views.SignUp, name='signup'),

    path('dashboard/', views.Dashboard, name='Dashboard'),
]