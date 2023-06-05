from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

from djoser.views import UserViewSet
from rest_framework import generics
from rest_framework.generics import DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import *
from .models import User, Invoice, Costs, Data
from .premissions import IsOwnerOrAdmin
from .serializers import *

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView

from djoser.conf import settings

class allUsers(generics.ListAPIView) : # Вывод данных всех пользователей
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = [IsAdminUser, ]

class UserProfile(generics.RetrieveUpdateAPIView) : # Данные пользователя
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_object(self):
        return self.request.user

class postMeterUser(generics.CreateAPIView) :  # Ввод показаний счетчика + сразу создается счет
    queryset = Data.objects.all()
    serializer_class = dataSerializer
    permission_classes = [IsAuthenticated,]



class updateMeter(generics.UpdateAPIView) :
    queryset = Data.objects.all()
    serializer_class = dataSerializer
    permission_classes = [IsOwnerOrAdmin,]
    lookup_url_kwarg = 'id'

    # def get_object(self):
    #     obj = self.queryset.get(userID=self.kwargs['id'])
    #     return obj
    # def perform_create(self, serializer):
    #     serializer.save(userID=self.request.user)

class allUserData(generics.RetrieveUpdateDestroyAPIView) :
    queryset = User.objects.all()
    serializer_class = UserDataSerializer
    lookup_url_kwarg = 'id'
    # permission_classes = [IsOwnerOrAdmin,]


class userData(generics.RetrieveAPIView) :
    queryset = User.objects.all()
    costs = Costs.objects.all()
    serializer_class = UserDataSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_object(self):
        return self.request.user

class deleteLastData(generics.DestroyAPIView) :
    queryset = Data.objects.all()
    serializer_class = dataSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_object(self):
        return self.queryset.order_by('-id').first()

class deleteDataById(generics.DestroyAPIView) :
    queryset = Data.objects.all()
    serializer_class = dataSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def get_object(self):
        obj = self.queryset.get(pk=self.kwargs['id'])
        return obj

class UserDataUpdateAPIView(APIView): # Для страницы администратора
    def put(self, request):
        data = request.data
        user_id = data.get('id')
        user_data = {
            'licSchet': data.get('licSchet'),
            'email': data.get('email'),
            'residents': data.get('residents'),
            'is_active' : data.get('is_active'),
            'is_staff' : data.get('is_staff')
        }
        data_objects = data.get('data')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(f"User with ID {user_id} does not exist.", status=status.HTTP_400_BAD_REQUEST)

        user_serializer = UserCustomSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Обновление объектов Data
        for data_obj in data_objects:
            data_id = data_obj.get('id')
            if data_id:
                try:
                    data_instance = Data.objects.get(id=data_id, userID=user)
                except Data.DoesNotExist:
                    return Response(f"Data object with ID {data_id} does not exist for user {user_id}.",
                                    status=status.HTTP_400_BAD_REQUEST)
                data_serializer = dataSerializer(data=data_obj, instance=data_instance)
            else:
                data_obj['userID'] = user.id
                data_serializer = dataSerializer(data=data_obj)

            if data_serializer.is_valid():
                data_serializer.save()
            else:
                return Response(data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("User data updated successfully.")
class UserDestroy(DestroyAPIView) :
    queryset = User.objects.all()
    lookup_field = 'pk'
    permission_classes = [IsAdminUser, ]

class UserCreateAPIView(CreateAPIView): # Создание пользователя админом
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsOwnerOrAdmin, ]

    def perform_create(self, serializer):
        password = serializer.validated_data.get('password')
        hashed_password = make_password(password)
        serializer.save(password=hashed_password)

