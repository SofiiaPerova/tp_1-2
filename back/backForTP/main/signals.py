from datetime import *

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

from main.models import Invoice, Data, User

# @receiver(pre_save, sender=Data)
# def CreateMeter(sender, instance, **kwargs):
#     data = instance
#     previous_record = Data.objects.filter(userID=data.userID).order_by('-date')[1]
#     if previous_record:
#         if (int(data.gas) < int(previous_record.gas)) :
#             raise ValidationError('Gas fields must be larger than the previous record')
#             if (int(data.water) < int(previous_record.water)) :
#                 raise ValidationError('Water fields must be larger than the previous record')
#             if (int(data.electro) <= int(previous_record.electro)) :
#                 raise ValidationError('Electro fields must be larger than the previous record')
#     instance.save()
@receiver(pre_save, sender=Data)
def check_previous_record(sender, instance, **kwargs):
    try:
        previous_record = Data.objects.filter(userID=instance.userID).order_by('-date')[0]
        if previous_record:
            if int(instance.gas) <= int(previous_record.gas):
                raise ValueError('Gas reading should be larger than the previous record')
            if int(instance.water) <= int(previous_record.water):
                raise ValueError('Water reading should be larger than the previous record')
            if int(instance.electro) <= int(previous_record.electro):
                raise ValueError('Electro reading should be larger than the previous record')
    except Data.DoesNotExist:
        pass

# @receiver(pre_save, sender=Data)
# def check(sender, instance, **kwargs) :
#     data = instance
#     user = User.objects.get(username=data.userID)
#     gas = data.gas
#     water = data.water
#     electro = data.electro
#     now = datetime.now()
#     if (user.data_set.count() > 0):
#         data2 = Data.objects.filter(userID=user.pk).order_by('-date')[0]
#
#         if (data2.date.month == now.month and data2.date.year == now.year) :
#
#             data2.gas = gas
#             data2.water = water
#             data2.electro = electro
#             data2.date = now
#             data2.save()
#
#             if (user.data_set.count() > 1):
#                 dataOneAgo = Data.objects.filter(userID=user.pk).order_by('-date')[1]
#                 invoice = Invoice.objects.filter(userID=user.pk).order_by('-date')[0]
#                 gasSumm = (int(gas) - int(dataOneAgo.gas)) * 6.9
#                 waterSumm = (int(water) - int(dataOneAgo.water)) * 28
#                 electroSumm = (int(electro) - int(dataOneAgo.electro)) * 4.85
#                 invoice.gasSumm = round(gasSumm,2)
#                 invoice.waterSumm = round(waterSumm,2)
#                 invoice.electroSumm = round(electroSumm,2)
#                 total = invoice.gasSumm + invoice.waterSumm + invoice.electroSumm + int(invoice.repairSumm) + int(invoice.trashSumm)
#                 invoice.total = total
#                 invoice.save()
#             else :
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

# @receiver(pre_save, sender=Data)
# def CreateInvoice(sender, instance, **kwargs):
#     data = instance
#     user = User.objects.get(username=data.userID)
#     gas = data.gas
#     water = data.water
#     electro = data.electro
#     now = datetime.now()
#
#     if (user.data_set.count() > 0) :
#         data2 = Data.objects.filter(userID=user.pk).order_by('-date')[0]
#
#
#         if (data2.date.month == now.month and data2.date.year == now.year) :
#
#             data2.gas = gas
#             data2.water = water
#             data2.electro = electro
#             data2.date = now
#
#
#             if (user.data_set.count() > 1):
#                 dataOneAgo = Data.objects.filter(userID=user.pk).order_by('-date')[1]
#                 invoice = Invoice.objects.filter(userID=user.pk).order_by('-date')[0]
#                 gasSumm = (int(gas) - int(dataOneAgo.gas)) * 6.9
#                 waterSumm = (int(water) - int(dataOneAgo.water)) * 28
#                 electroSumm = (int(electro) - int(dataOneAgo.electro)) * 4.85
#                 invoice.gasSumm = round(gasSumm,2)
#                 invoice.waterSumm = round(waterSumm,2)
#                 invoice.electroSumm = round(electroSumm,2)
#                 total = invoice.gasSumm + invoice.waterSumm + invoice.electroSumm + int(invoice.repairSumm) + int(invoice.trashSumm)
#                 invoice.total = total
#                 invoice.save()
#             else :
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
#             gas = (int(gas) - int(data2.gas))*6.9
#             water = (int(water) - int(data2.water))*28
#             electro = (int(electro) - int(data2.electro))*4.85
#             Invoice.objects.create(
#                 gasSumm = round(gas,2),
#                 waterSumm = round(water,2),
#                 electroSumm = round(electro,2),
#                 trashSumm = 100,
#                 repairSumm = 100,
#                 total = gas + water + electro + 200,
#                 userID=data.userID
#             )
#     else: Invoice.objects.create(
#                 gasSumm = round(int(gas) * 6.9),
#                 waterSumm = round(int(water) * 28),
#                 electroSumm = round(int(electro) * 4.85),
#                 trashSumm = 100,
#                 repairSumm = 100,
#                 total = int(gas) + int(water) + int(electro) + 200,
#                 userID=data.userID
#         )

# @receiver(post_save, sender=Data)
# def DeleteInvoiceMeter(sender, instance, **kwargs):
#     total_records = Invoice.objects.count()
#
#     if total_records > 3:
#         num_records_to_delete = total_records - 3
#
#         invoices_to_delete = Invoice.objects.order_by('-date')[3:]
#
#         for invoice in invoices_to_delete:
#             invoice.delete()
#
#     total_records = Data.objects.count()
#
#     if total_records > 3:
#         num_records_to_delete = total_records - 3
#
#         data_to_delete = Data.objects.order_by('-date')[3:(3 + num_records_to_delete)]
#
#         for data in data_to_delete:
#             data.delete()