from django.urls import path,include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
				path('', views.index, name='index'),
                path('login/', views.login, name='login'),
                path('register/', views.register, name='register'),
                path('logout/', views.logout, name='logout'),
                path('home/', views.home, name='home'),
                ########### CURRENT URLS ##########################
                path('sendmsg/', views.addmsg, name='sendmsg'),
                path('jobpost/', views.jobpost_create, name='jobpost'),
                path('home/jobpost/', views.jobpost_create, name='jobpost'),
                path('viewmsg/', views.viewmsg, name='viewmsg'),
                path('search/', views.searchjob, name='search'),
                path('auto/', views.searchindustry, name='auto'),
                path('searchJob/', views.searchjobb, name='searchJob'),
                path('createresume/', views.createresume, name='createresume'),
                path('show/', views.show, name='show'),
                path('updateresume/<str:pk>/', views.updateresume, name='updateresume'),
                
]