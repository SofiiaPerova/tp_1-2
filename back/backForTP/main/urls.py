from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

app_name = 'main'

urlpatterns = [
    path('admin/user/<id>/', allUserData.as_view()),  # Вывод всей информации по пользователю для Админки
    path('admin/users/', allUsers.as_view()),  # Вывод всех пользователей

    path('user/inputMeter/', postMeterUser.as_view()),  # Ввод показаний со счетчиков
    path('user/updateMeter/<int:id>/', updateMeter.as_view()), # Обновление данных
    path('user/profile/', UserProfile.as_view()),  # Данные пользователя
    path('user/userData/', userData.as_view()), # Вся информация по опльзователю
    path('user/deleteData/', deleteLastData.as_view()), # Удаление последний показаний
    path('user/deleteData/<int:id>/', deleteDataById.as_view()), # Удаление показаний по id Data



    path('user/update/', UserDataUpdateAPIView.as_view(), name='user-update'),
]