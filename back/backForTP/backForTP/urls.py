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

    path('admin/', admin.site.urls),                                                        # Админка
    path('api/v1/admin/create/', AdminRegistrationView.as_view()),
    path('api/v1/admin/user/<id>', allUserData.as_view()),                                  # Вывод всей информации по пользователю для Админки
    path('api/v1/users/', allUsers.as_view()),                                              # Вывод всех пользователей


    path('api/v1/user/inputMeter/', postMeterUser.as_view()),                               # Ввод показаний со счетчиков
    path('api/v1/user/statistics/meter/all/', getAllMeterUser.as_view()),                   # Все показания пользователя
    path('api/v1/user/statistics/meter/', getMeterUser.as_view()),                          # Показания пользователя за 3 месяца
    path('api/v1/user/statistics/invoice/all/', getAllInvoiceUser.as_view()),               # Все квитанции
    path('api/v1/user/statistics/invoice/<int:monthsAgo>/', getInvoiceUser.as_view()),      # Квитанция с указаниям месца ( 1 - прошлый месяц, 2 - пазопрошлый, 3 - два месяца назад)
    path('api/v1/user/profile/', UserProfile.as_view()),                                    # Данные пользователя
    path('api/v1/user/getGasMeter/', getGasMeter.as_view()),                                # Траты газа за 3 месяца
    path('api/v1/user/getWaterMeter/', getWaterMeter.as_view()),                            # Траты воды за 3 месяца
    path('api/v1/user/getElectroMeter/', getElectroMeter.as_view()),                        # Траты энергии за 3 месяца
    path('api/v1/user/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'), #Активация аккаунта


    path('auth/', include('djoser.urls')),          # регистрация и авторизация
    path('auth/', include('djoser.urls.jwt')),      # получение токена

]

urlpatterns += swagger # url для сваггера
