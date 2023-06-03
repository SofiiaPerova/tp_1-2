from datetime import *

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError
from datetime import date
from main.models import *



@receiver(pre_save, sender=Data) # Валидация показателей
def check_previous_record(sender, instance, **kwargs):
    try:

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

@receiver(post_save, sender=Data) # Удаление старых показателей
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

