from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
import jwt
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError

class User(AbstractUser) :
    licSchet = models.CharField("Лицевой Счет",max_length=11, unique=True)
    date = models.DateField("Дата создания аккаунта", auto_now_add=True)
    username = models.EmailField("Почта", unique=True)
    residents = models.IntegerField("Кол-во жильцов", default=3)


    REQUIRED_FIELDS = ['licSchet','is_superuser']

    def __str__(self):
        return self.username

class Invoice(models.Model) :
    gasSumm = models.CharField("Сумма за газ", max_length=10)
    waterSumm = models.CharField("Сумма за воду", max_length=10)
    electroSumm = models.CharField("Сумма за энергию", max_length=10)
    trashSumm = models.CharField("Сумма за мусор", max_length=10)
    repairSumm = models.CharField("Сумма за обслуживание дома", max_length=10)
    total = models.CharField("Общая сумма", max_length=10)
    date = models.DateTimeField("Дата создания квитанции", auto_now_add=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date.year}.{self.date.month}.{self.date.day}"

class Data(models.Model) :
    gas = models.CharField("Показания газового счетчика", max_length=10)
    water = models.CharField("Показания водяного счетчика", max_length=10)
    electro = models.CharField("Показания счетчика энергии",  max_length=10)
    date = models.DateTimeField("Дата внесения показаний", auto_now_add=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    costs = models.OneToOneField('Costs', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.date.year}.{self.date.month}.{self.date.day}"

class Costs(models.Model) :
    gasCost = models.CharField("Потребление газа", max_length=10)
    waterCost = models.CharField("Потребление воды", max_length=10)
    electroCost = models.CharField("Потребление энергии", max_length=10)
    date = models.DateTimeField("Дата внесения показаний", auto_now_add=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)

    def __str__(self):
        return f"{self.date.year}.{self.date.month}.{self.date.day}"