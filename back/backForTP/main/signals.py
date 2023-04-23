from datetime import *

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

from main.models import *



@receiver(pre_save, sender=Costs)
def check_previous_record(sender, instance, **kwargs):
    try:
        instance = instance.data
        user = User.objects.get(email=instance.userID)
        if user.data.count() > 0 :
            previous_record = Data.objects.filter(userID=instance.userID).order_by('-date')[0]
            if previous_record:
                if int(instance.gas) <= int(previous_record.gas):
                    raise ValueError('Показания газа должны быть больше предыдущих')
                if int(instance.water) <= int(previous_record.water):
                    raise ValueError('Показания воды должны быть больше предыдущих')
                if int(instance.electro) <= int(previous_record.electro):
                    raise ValueError('Показания энергии должны быть больше предыдущих')
    except Data.DoesNotExist:
        pass

@receiver(pre_save, sender=Data)
def createCosts(sender, instance, **kwargs) :
    data1 = instance
    user = User.objects.get(email=data1.userID)
    if (user.data.count() > 0) :
        data2 = Data.objects.filter(userID=user.pk).order_by('-date')[0]
        gas = int(data1.gas) - int(data2.gas)
        water = int(data1.water) - int(data2.water)
        electro = int(data1.electro) - int(data2.electro)
    else:
        gas = data1.gas
        water = data1.water
        electro =  data1.electro
    if int(gas) <= 0 :
        raise ValidationError('Показания газа должны быть больше предыдущих')
    if int(water) <= 0 :
        raise ValidationError('Показания воды должны быть больше предыдущих')
    if int(electro) <= 0 :
        raise ValidationError('Показания энергии должны быть больше предыдущих')
    cost = Costs.objects.create(gasCost = gas, waterCost = water, electroCost = electro,
                                userID = user)
    data1.costs = cost
    cost.save()


@receiver(post_save, sender=Data)
def createInvoice(sender, instance, **kwargs) :
    user = User.objects.get(email = instance.userID)
    instance = instance.costs
    gasSumm = int(int(instance.gasCost) * 6.9)
    waterSumm = int(int(instance.waterCost) * 28)
    electroSumm = int(int(instance.electroCost) * 4.85)
    trashSumm = int(user.residents) * 100
    Invoice.objects.create(
        gasSumm =  gasSumm,
        waterSumm = waterSumm,
        electroSumm = electroSumm,
        trashSumm = trashSumm,
        repairSumm = 200,
        total = gasSumm + electroSumm + waterSumm + trashSumm + 100,
        userID = user
    )




@receiver(post_save, sender=Data)
def DeleteInvoiceMeter(sender, instance, **kwargs):
    total_records = Invoice.objects.filter(userID = instance.userID).count()

    if total_records > 5:
        num_records_to_delete = total_records - 5

        invoices_to_delete = Invoice.objects.filter(userID = instance.userID).order_by('-date')[5:(5 + num_records_to_delete)]

        for invoice in invoices_to_delete:
            invoice.delete()

    total_records = Data.objects.filter(userID = instance.userID).count()

    if total_records > 5:
        num_records_to_delete = total_records - 5

        data_to_delete = Data.objects.filter(userID = instance.userID).order_by('-date')[5:(5 + num_records_to_delete)]

        for data in data_to_delete:
            data.delete()

    total_records = Costs.objects.filter(userID=instance.userID).count()

    if total_records > 5:
        num_records_to_delete = total_records - 5

        costs_to_delete = Costs.objects.filter(userID=instance.userID).order_by('-date')[5:(5 + num_records_to_delete)]

        for cost in costs_to_delete:
            cost.delete()

