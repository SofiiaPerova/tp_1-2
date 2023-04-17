from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import *
from .models import *
from .premissions import IsOwnerOrAdmin
from .serializers import dataSerializer, UserSerializer, UserCustomSerializer, dataSerializer, invoiceSerializer


class allUsers(generics.ListAPIView) :
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer

class UserProfile(generics.ListCreateAPIView) : # Данные пользователя
    queryset = User.objects.all()
    serializer_class = UserCustomSerializer
    permission_classes = [IsOwnerOrAdmin, ]


class postMeterUser(generics.CreateAPIView) :  # Ввод показаний счетчика + сразу создается счет
    queryset = Data.objects.all()
    serializer_class = dataSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(userID=self.request.user)


    # def deleteOld(self):
    # def create(self, request, *args, **kwargs):
    #     data = request
    #     user = User.objects.get(username=data.userID)
    #     gas = data.gas
    #     water = data.water
    #     electro = data.electro
    #     now = datetime.now()
    #
    #     if (user.data_set.count() > 0):
    #         data2 = Data.objects.filter(userID=user.pk).order_by('-date')[0]
    #
    #         if (data2.date.month == now.month and data2.date.year == now.year):
    #
    #             data2.gas = gas
    #             data2.water = water
    #             data2.electro = electro
    #             data2.date = now
    #
    #             if (user.data_set.count() > 1):
    #                 dataOneAgo = Data.objects.filter(userID=user.pk).order_by('-date')[1]
    #                 invoice = Invoice.objects.filter(userID=user.pk).order_by('-date')[0]
    #                 gasSumm = (int(gas) - int(dataOneAgo.gas)) * 6.9
    #                 waterSumm = (int(water) - int(dataOneAgo.water)) * 28
    #                 electroSumm = (int(electro) - int(dataOneAgo.electro)) * 4.85
    #                 invoice.gasSumm = round(gasSumm, 2)
    #                 invoice.waterSumm = round(waterSumm, 2)
    #                 invoice.electroSumm = round(electroSumm, 2)
    #                 total = invoice.gasSumm + invoice.waterSumm + invoice.electroSumm + int(invoice.repairSumm) + int(
    #                     invoice.trashSumm)
    #                 invoice.total = total
    #                 invoice.save()
    #             else:
    #                 invoice = Invoice.objects.filter(userID=user.pk).order_by('-date')[0]
    #                 gasSumm = int(gas) * 6.9
    #                 waterSumm = int(water) * 28
    #                 electroSumm = int(electro) * 4.85
    #                 invoice.gasSumm = round(gasSumm, 2)
    #                 invoice.waterSumm = round(waterSumm, 2)
    #                 invoice.electroSumm = round(electroSumm, 2)
    #                 invoice.repairSumm = 100
    #                 invoice.trashSumm = 100
    #                 invoice.total = invoice.gasSumm + invoice.waterSumm + invoice.electroSumm + invoice.repairSumm + invoice.trashSumm
    #                 invoice.save()
    #
    #
    #
    #
    #         else:
    #             gas = (int(gas) - int(data2.gas)) * 6.9
    #             water = (int(water) - int(data2.water)) * 28
    #             electro = (int(electro) - int(data2.electro)) * 4.85
    #             Invoice.objects.create(
    #                 gasSumm=round(gas, 2),
    #                 waterSumm=round(water, 2),
    #                 electroSumm=round(electro, 2),
    #                 trashSumm=100,
    #                 repairSumm=100,
    #                 total=gas + water + electro + 200,
    #                 userID=data.userID
    #             )
    #     else:
    #         Invoice.objects.create(
    #             gasSumm=round(int(gas) * 6.9),
    #             waterSumm=round(int(water) * 28),
    #             electroSumm=round(int(electro) * 4.85),
    #             trashSumm=100,
    #             repairSumm=100,
    #             total=int(gas) + int(water) + int(electro) + 200,
    #             userID=data.userID
    #         )
    #
    #     Invoice.objects.filter(userID=self.request.user.pk).order_by('-date')[3:].delete()
    #     Data.objects.filter(userID=self.request.user.pk).order_by('-date')[3:].delete()

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
        user = get_object_or_404(User, username=self.request.user.username)
        costs = Costs.objects.filter(userID=user).order_by('-id')[:3]
        gas_costs = [cost.gasCost for cost in costs]
        return JsonResponse({'gas_costs': gas_costs})



class getWaterMeter(APIView) : # Вывод трат воды за 3 месяца
    def get(self, request):
        user = get_object_or_404(User, username=self.request.user.username)
        costs = Costs.objects.filter(userID=user).order_by('-id')[:3]
        gas_costs = [cost.waterCosts for cost in costs]
        return JsonResponse({'water_costs': gas_costs})


class getElectroMeter(APIView) : # Вывод трат энергии за 3 месяца
    def get(self, request):
        user = get_object_or_404(User, username=self.request.user.username)
        costs = Costs.objects.filter(userID=user).order_by('-id')[:3]
        gas_costs = [cost.electroCost for cost in costs]
        return JsonResponse({'electro_costs': gas_costs})



