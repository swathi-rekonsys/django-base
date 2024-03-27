"""
URL configuration for userregistration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from userregistrationapp import views

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # URL patterns for different views
    path('', views.SingupPage, name='singup'),  # URL for signup page
    path('login/', views.LoginPage, name='login'),  # URL for login page
    path('home/', views.HomePage, name='home'),  # URL for home page
    path('logout/', views.LogoutPage, name='logout'),  # URL for logout page
]
