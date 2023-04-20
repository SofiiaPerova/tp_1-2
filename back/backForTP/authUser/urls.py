from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView
from django.urls import path, include

from authUser.views import *

urlpatterns = [
    path('activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'), # Активация аккаунта
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),  # Тут вводим почту
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),# Страница, говорящая об отправленном письме
    path('password/reset/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Сюда отправляем password + re_password
    path('password/reset/complite/', PasswordResetCompleteView.as_view(), name='password_reset_complete'), # Страница, говорящая об успешной смене пароля

    path('admin/create/', AdminRegistrationView.as_view()), # Регистрация админа
    path('', include('djoser.urls')),  # регистрация и авторизация
    path('', include('djoser.urls.jwt')),  # получение токена
]

