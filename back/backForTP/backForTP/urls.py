"""backForTP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from main.views import *
from .yasg import urlpatterns as swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', allUsers.as_view()),
    path('api/v1/user/inputMeter/', postMeterUser.as_view()),
    path('api/v1/user/statistics/meter/all/', getAllMeterUser.as_view()),
    path('api/v1/user/statistics/meter/', getMeterUser.as_view()),
    path('api/v1/user/statistics/invoice/all/', getAllInvoiceUser.as_view()),
    path('api/v1/user/statistics/invoice/<pk>/', getInvoiceUser.as_view()),
    path('api/v1/user/profile/', UserProfile.as_view()),


    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]

urlpatterns += swagger
