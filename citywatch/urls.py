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
    path('signin/', views.SignIn, name='signin'),
    path('signup/', views.SignUp, name='signup'),

    path('dashboard/', views.Dashboard, name='Dashboard'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)