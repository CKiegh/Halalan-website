"""PhilippineNationalElection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.homepage, name="homepage"),
    path('', views.loginpage, name="loginpage"),
    path('signup/', views.signuppage, name="signuppage"),
    path('users/', views.userspage, name="userspage"),
    path('base/', views.base, name="base"),
    path('candidates/', views.candidatespage, name="candidatespage"),
    path('about/', views.aboutpage, name="aboutpage"),
    path('updateuser/', views.updateuserpage, name="updateuserpage"),
    path('votes/', views.votespage, name="votespage"),
]
