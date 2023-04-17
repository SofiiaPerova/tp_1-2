from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
import jwt
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

class User(AbstractUser) :
    licSchet = models.CharField(max_length=11, unique=True)
    # username = models.EmailField(unique=True)
    date = models.DateField(auto_now_add=True)
    username = models.EmailField(unique=True)
    residents = models.IntegerField(default=3)


    REQUIRED_FIELDS = ['licSchet','is_superuser']

    def __str__(self):
        return self.username

class Invoice(models.Model) :
    gasSumm = models.CharField(max_length=10)
    waterSumm = models.CharField(max_length=10)
    electroSumm = models.CharField(max_length=10)
    trashSumm = models.CharField(max_length=10)
    repairSumm = models.CharField(max_length=10)
    total = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

class Data(models.Model) :
    gas = models.CharField(max_length=10)
    water = models.CharField(max_length=10)
    electro = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    costs = models.OneToOneField('Costs', on_delete=models.CASCADE, null=True)

class Costs(models.Model) :
    gasCost = models.CharField(max_length=10)
    waterCost = models.CharField(max_length=10)
    electroCost = models.CharField(max_length=10)
    userID = models.CharField(max_length=30)


    # def save(self, *args, **kwargs):
    #         previous_record = Data.objects.filter(userID=self.userID).order_by('-date').last()
    #         if previous_record:
    #             if (int(self.gas) < int(previous_record.gas)) :
    #                 raise ValidationError('Gas fields must be larger than the previous record')
    #             if (int(self.water) < int(previous_record.water)) :
    #                 raise ValidationError('Water fields must be larger than the previous record')
    #             if (int(self.electro) <= int(previous_record.electro)) :
    #                 raise ValidationError('Electro fields must be larger than the previous record')
    #         super().save(*args, **kwargs)

    # def clean(self):
    #     super().clean()
    #     previous_records = Data.objects.filter(userID=self.userID).order_by('-date')[:2]
    #     if previous_records.count() == 0:
    #         return
    #     previous_record = previous_records[0]
    #     if int(self.gas) <= int(previous_record.gas) or int(self.water) <= int(previous_record.water) or int(
    #             self.electro) <= int(previous_record.electro):
    #         raise ValidationError('Gas, water, and electro fields must be larger than the previous record')






# @receiver(post_save, sender = dataMeter)
# def createData(instance, **kwargs) :
#     dataMeter = instance
#     if User.objects.filter(username=user.email).exists():
#         return
#     else:
#         Gas.objects.create(userID = user.username)
#         Water.objects.create(userID=user.username)
#         Electricity.objects.create(userID=user.username)
#         Data.objects.create(userID=user.username, gas_id = user.username, water_id = user.username, electricity_id = user.username)
#         user.data_id = user.username
