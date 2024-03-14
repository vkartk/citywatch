from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('reports/', views.reports, name='reports'),
    path('report/', views.report, name='report'),
    path('issue/<int:id>/', views.IssuePage, name='IssuePage'),
    path('search/', views.Search, name='Search'),

    path('signin/', views.SignIn, name='signin'),
    path('signup/', views.SignUp, name='signup'),
    path('signout/', views.SignOut, name='signout'),

    path('dashboard/', views.Dashboard, name='Dashboard'),
    path('staff/', views.StaffDashboard, name='StaffDashboard'),

    path('api/issues/', views.IssueAPI, name='IssueAPI'),
    path('api/issue/<int:id>/', views.IssueAPI, name='IssueAPI'),
    path('api/categories/', views.CategoryAPI, name='CategoryAPI'),
    path('api/category/<int:id>/', views.CategoryAPI, name='CategoryAPI'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)