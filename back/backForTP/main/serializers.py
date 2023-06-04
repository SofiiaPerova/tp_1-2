from djoser.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *

class UserCustomSerializer(serializers.ModelSerializer) :
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['id', 'licSchet', 'email', 'residents', 'username', 'is_active', 'first_name', 'second_name', 'last_name', 'is_staff']

class UserCreateSerializer(serializers.ModelSerializer):
    is_staff = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=False)
    class Meta:
        model = User
        fields = ['email', 'licSchet', 'password', 'is_staff', 'is_active']




class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

    def create(self, validated_data):
        # Получить пользователя на основе текущего запроса или другой доступной информации
        user = self.context['request'].user

        # Создать экземпляр Data с переданными данными
        if len(str(validated_data['gas'])) >= 6:
            raise ValueError('Показания газа должны содержать менее 6 цифр')
        if len(str(validated_data['water'])) >= 6:
            raise ValueError('Показания воды должны содержать менее 6 цифр')
        if len(str(validated_data['electro'])) >= 6:
            raise ValueError('Показания энергии должны содержать менее 6 цифр')

        if user.data.count() > 0 :

            previous_record = Data.objects.filter(userID=user).order_by('-date')[0]
            if previous_record:
                if int(validated_data['gas']) <= int(previous_record.gas):
                    raise ValueError('Показания газа должны быть больше предыдущих')
                if int(validated_data['water']) <= int(previous_record.water):
                    raise ValueError('Показания воды должны быть больше предыдущих')
                if int(validated_data['electro']) <= int(previous_record.electro):
                    raise ValueError('Показания энергии должны быть больше предыдущих')

        data = Data.objects.create(userID=user, **validated_data)

        # Создать экземпляр Costs
        if user.data.count() > 1:
            print(user.data.count())
            data2 = Data.objects.order_by('-date')[1]
            gas = int(data.gas) - int(data2.gas)
            water = int(data.water) - int(data2.water)
            electro = int(data.electro) - int(data2.electro)
        else:
            gas = data.gas
            water = data.water
            electro = data.electro
        cost = Costs.objects.create(gasCost=gas, waterCost=water, electroCost=electro, userID=user, data=data)

        # Создать экземпляр Invoice
        gasSumm = int(int(cost.gasCost) * 6.9)
        waterSumm = int(int(cost.waterCost) * 28)
        electroSumm = int(int(cost.electroCost) * 4.85)
        trashSumm = int(int(user.residents) * 100)
        total = gasSumm + electroSumm + waterSumm + trashSumm + 200
        invoice = Invoice.objects.create(gasSumm=gasSumm, waterSumm=waterSumm, electroSumm=electroSumm,
                                         trashSumm=trashSumm, repairSumm=200, total=total, userID=user, data=data)

        return data

    def update(self, instance, validated_data):
        # Обновить экземпляр Data
        instance.gas = validated_data.get('gas', instance.gas)
        instance.water = validated_data.get('water', instance.water)
        instance.electro = validated_data.get('electro', instance.electro)
        instance.save()

        # Обновить экземпляр Costs
        user = instance.userID
        if user.data.count() > 1:
            data2 = Data.objects.order_by('-date')[1]
            if data2.date != instance.date :
                gas = int(instance.gas) - int(data2.gas)
                water = int(instance.water) - int(data2.water)
                electro = int(instance.electro) - int(data2.electro)
            else:
                gas = instance.gas
                water = instance.water
                electro = instance.electro
        else:
            gas = instance.gas
            water = instance.water
            electro = instance.electro

        cost = instance.cost  # Предполагается, что связь OneToOne называется "cost"
        cost.gasCost = gas
        cost.waterCost = water
        cost.electroCost = electro
        cost.save()

        # Обновить экземпляр Invoice
        gasSumm = int(int(gas) * 6.9)
        waterSumm = int(int(water) * 28)
        electroSumm = int(int(electro) * 4.85)
        trashSumm = int(int(user.residents) * 100)
        total = gasSumm + electroSumm + waterSumm + trashSumm + 200

        invoice = instance.invoice  # Предполагается, что связь OneToOne называется "invoice"
        invoice.gasSumm = gasSumm
        invoice.waterSumm = waterSumm
        invoice.electroSumm = electroSumm
        invoice.trashSumm = trashSumm
        invoice.total = total
        invoice.save()

        return instance

class invoiceSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Invoice
        fields = '__all__'

class CostsSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Costs
        fields = '__all__'


class UserDataSerializer(serializers.ModelSerializer) :
    data = dataSerializer(many=True)
    invoice = invoiceSerializer(many=True)
    costs = CostsSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'licSchet', 'email', 'residents', 'data', 'costs', 'invoice', 'first_name', 'second_name', 'last_name', 'is_staff', 'is_active']









