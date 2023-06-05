from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from django.urls import path, include

from authUser.views import *

urlpatterns = [
    path('activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'), # Активация аккаунта
    path('password/reset/', sendEmail.as_view(), name='password_reset'),  # Тут вводим почту для восстановления пароля
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),# Страница, говорящая об отправленном письме
    path('password/reset/confirm/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complite/', PasswordResetCompleteView.as_view(), name='password_reset_complete'), # Страница, говорящая об успешной смене пароля

    path('', include('djoser.urls')),  # регистрация и авторизация
    path('', include('djoser.urls.jwt')),  # получение токена


]

