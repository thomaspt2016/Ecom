"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from loginfo import views
app_name = 'loginfo'

urlpatterns = [
    path('signup',views.SignupView.as_view(),name='signup'),
    path('login',views.SigninView.as_view(),name='login'),
    path('verifyotp', views.OtpVerificationView.as_view(), name="verifyotp"),
    path('logout', views.SignoutView.as_view(), name='logout'),
    path('superadmin',views.SuperAdminView.as_view(),name='superadmin')
]
