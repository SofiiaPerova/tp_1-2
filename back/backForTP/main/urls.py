from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

app_name = 'main'

urlpatterns = [
    path('admin/user/<id>', allUserData.as_view()),  # Вывод всей информации по пользователю для Админки
    path('admin/users/', allUsers.as_view()),  # Вывод всех пользователей

    path('user/inputMeter/', postMeterUser.as_view()),  # Ввод показаний со счетчиков
    path('user/statistics/meter/all/', getAllMeterUser.as_view()),  # Все показания пользователя
    path('user/statistics/meter/', getMeterUser.as_view()),  # Показания пользователя за 3 месяца
    path('user/statistics/invoice/all/', getAllInvoiceUser.as_view()),  # Все квитанции
    path('user/statistics/invoice/<int:monthsAgo>/', getInvoiceUser.as_view()), # Квитанция с указаниям месца ( 1 - прошлый месяц, 2 - пазопрошлый, 3 - два месяца назад)
    path('user/profile/', UserProfile.as_view()),  # Данные пользователя
    path('user/getGasMeter/', getGasMeter.as_view()),  # Траты газа за 3 месяца
    path('user/getWaterMeter/', getWaterMeter.as_view()),  # Траты воды за 3 месяца
    path('user/getElectroMeter/', getElectroMeter.as_view()),  # Траты энергии за 3 месяца


    path('user/userData/', userData.as_view()), # Вся информация по опльзователю


]