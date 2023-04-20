from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.decorators.csrf import csrf_exempt
from djoser.views import UserViewSet
from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from backForTP import settings
from main.models import User
from main.serializers import AdminSerializer


# Create your views here.
@csrf_exempt
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

@csrf_exempt
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