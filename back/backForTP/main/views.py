from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.http import JsonResponse
from djoser.views import UserViewSet
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import *
from .models import *
from .premissions import IsOwnerOrAdmin
from .serializers import *

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView

from djoser.conf import settings

class CustomPasswordResetView(PasswordResetView):
    def send_email(self, context):
        """Отправляет email с ссылкой на сброс пароля"""
        to = [self.email]
        # Генерируем токен и кодируем его для добавления в ссылку
        token = default_token_generator.make_token(self.user)
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        # Собираем ссылку для сброса пароля
        reset_url = f"{settings.PASSWORD_RESET_CONFIRM_URL}?uid={uid}&token={token}"
        # Формируем текст и тему email-сообщения
        subject = 'Сброс пароля'
        message = f"Здравствуйте! На этой странице вы можете сбросить свой пароль: {reset_url}"
        # Отправляем email-сообщение
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, to, fail_silently=False)

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        # Проверяем, что токен верен
        if not default_token_generator.check_token(user, serializer.validated_data['token']):
            return Response({'token': ['Недействительный токен']}, status=status.HTTP_400_BAD_REQUEST)
        # Устанавливаем новый пароль
        new_password = serializer.validated_data['new_password']
        user.set_password(new_password)
        user.save()
        # Возвращаем успешный ответ
        return Response({'detail': 'Пароль успешно изменен'})

class ActivateUser(UserViewSet):   # Активация аккаунта по ссылке на почту
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        # this line is the only change from the base implementation.
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}

        return serializer_class(*args, **kwargs)

    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminRegistrationView(generics.CreateAPIView) : # Регистрация админа
    queryset = User.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdminUser, ]

class allUsers(generics.ListAPIView) : # Вывод данных всех пользователей
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = [IsAdminUser, ]

class UserProfile(generics.RetrieveUpdateAPIView) : # Данные пользователя
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = [IsOwnerOrAdmin, ]


class postMeterUser(generics.CreateAPIView) :  # Ввод показаний счетчика + сразу создается счет
    queryset = Data.objects.all()
    serializer_class = dataSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(userID=self.request.user)


class getAllInvoiceUser(generics.ListAPIView) : # Выдает все счета
    queryset = Invoice.objects.all()
    serializer_class = invoiceSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_queryset(self):
        user = self.request.user
        return Invoice.objects.filter(userID=user)

class getAllMeterUser(generics.ListAPIView) : # Выдает все показатели
    queryset = Data.objects.all()
    serializer_class = dataSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_queryset(self):
        user = self.request.user
        return Data.objects.filter(userID=user)

class getInvoiceUser(APIView) :  # Выдает счета за последние 3 месяца при указании месяца ( pk )
    def get(self, request,monthsAgo):
        monthsAgo = int(monthsAgo)
        if (monthsAgo > 3 or monthsAgo < 1):
            return Exception
        invoice = Invoice.objects.filter(userID = self.request.user.pk).order_by('-date')[monthsAgo-1:monthsAgo]
        serializer = invoiceSerializer(invoice, many=True)
        return Response(serializer.data)

class getMeterUser(APIView) : ## Выдает показания за последние 3 месяца
    def get(self, request):
        meter = Data.objects.filter(userID = self.request.user.pk).order_by('-date')[:3]
        serializer = dataSerializer(meter, many=True)
        return Response(serializer.data)


class getGasMeter(APIView) : # Вывод трат газа за 3 месяца
    def get(self, request):
        user = get_object_or_404(User, email=self.request.user.email)
        costs = Costs.objects.filter(userID=user).order_by('-id')[:3]
        gas_costs = [cost.gasCost for cost in costs]
        return JsonResponse({'gas_costs': gas_costs})



class getWaterMeter(APIView) : # Вывод трат воды за 3 месяца
    def get(self, request):
        user = get_object_or_404(User, email=self.request.user.email)
        costs = Costs.objects.filter(userID=user).order_by('-id')[:3]
        gas_costs = [cost.waterCost for cost in costs]
        return JsonResponse({'water_costs': gas_costs})


class getElectroMeter(APIView) : # Вывод трат энергии за 3 месяца
    def get(self, request):
        user = get_object_or_404(User, email=self.request.user.email)
        costs = Costs.objects.filter(userID=user).order_by('-id')[:3]
        gas_costs = [cost.electroCost for cost in costs]
        return JsonResponse({'electro_costs': gas_costs})


class allUserData(generics.RetrieveUpdateDestroyAPIView) :
    queryset = User.objects.all()
    serializer_class = AdminSerializer
    lookup_url_kwarg = 'id'
    permission_classes = [IsAdminUser,]
    # dd





