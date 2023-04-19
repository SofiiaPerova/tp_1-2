from django.http import JsonResponse
from djoser.views import UserViewSet
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import *
from .models import *
from .premissions import IsOwnerOrAdmin
from .serializers import *



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





