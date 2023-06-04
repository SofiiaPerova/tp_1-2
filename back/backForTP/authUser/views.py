from coreapi.compat import force_text
from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.core.mail import send_mail
from django.shortcuts import redirect

from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from djoser.views import UserViewSet

from rest_framework import status, generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from backForTP import settings
from main.models import User
from main.serializers import AdminRegistrationSerializer


class sendEmail(APIView) :
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.get(email=email)
        # Генерация токена для пользователя
        token = PasswordResetTokenGenerator().make_token(user)
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))

        # Формирование ссылки на страницу сброса пароля на frontend
        reset_url = 'http://' + settings.FRONTEND_URL + '/recovery_pass_2/' + uidb64 + "/" + token + "/"

        # Отправка письма на электронную почту пользователя
        send_mail(
            'Сброс пароля',
            f'Перейдите по ссылке, чтобы сбросить пароль: {reset_url}',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return Response({'detail': 'Ссылка на страницу сброса пароля отправлена на указанную почту.'})


class CustomPasswordResetConfirmView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and PasswordResetTokenGenerator().check_token(user, token):
            password = request.data.get('password')
            re_password = request.data.get('re_password')
            if password and re_password and password == re_password:
                user.password = make_password(password)
                user.save()
                return Response({'status': 'password updated'})
            else:
                return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Token is invalid or has expired'}, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
# @csrf_exempt
#
# class CustomPasswordResetView(PasswordResetView):
#
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#     def send_email(self, **kwargs):
#         """Отправляет email с ссылкой на сброс пароля"""
#         to = [self.email]
#         # Генерируем токен и кодируем его для добавления в ссылку
#         token = default_token_generator.make_token(self.user)
#         uid = urlsafe_base64_encode(force_bytes(self.user.pk))
#         # Собираем ссылку для сброса пароля
#         url = "http://localhost:8080/recovery_pass_2/"
#         reset_url = f"{url}?uid={uid}&token={token}"
#         # Формируем текст и тему email-сообщения
#         subject = 'Сброс пароля'
#         message = f"Здравствуйте! На этой странице вы можете сбросить свой пароль: {reset_url}"
#         # Отправляем email-сообщение
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, to, fail_silently=False)
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.user = serializer.validated_data['user']
#         self.email = self.user.email
#         self.send_email()
#         return Response({'detail':('Password reset e-mail has been sent.')})
#
# @csrf_exempt
# class CustomPasswordResetConfirmView(PasswordResetConfirmView):
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.user
#         # Проверяем, что токен верен
#         if not default_token_generator.check_token(user, serializer.validated_data['token']):
#             return Response({'token': ['Недействительный токен']}, status=status.HTTP_400_BAD_REQUEST)
#         # Устанавливаем новый пароль
#         new_password = serializer.validated_data['new_password']
#         user.set_password(new_password)
#         user.save()
#         # Возвращаем успешный ответ
#         return Response({'detail': 'Пароль успешно изменен'})
#
class ActivateUser(UserViewSet):   # Активация аккаунта по ссылке на почту
    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())

        # this line is the only change from the base implementation.
        kwargs['data'] = {"uid": self.kwargs['uid'], "token": self.kwargs['token']}

        return serializer_class(*args, **kwargs)

    def activation(self, request, uid, token, *args, **kwargs):
        super().activation(request, *args, **kwargs)
        return redirect(('http://45.146.164.34:5000/authorization'))




class AdminRegistrationView(generics.CreateAPIView) : # Регистрация админа
    queryset = User.objects.all()
    serializer_class = AdminRegistrationSerializer
    permission_classes = [IsAdminUser, ]
