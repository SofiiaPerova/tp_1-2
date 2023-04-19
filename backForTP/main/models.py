from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from .validators import *



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin) :
    licSchet = models.CharField("Лицевой Счет",max_length=11, unique=True, validators=[validate_licSchet])
    date = models.DateField("Дата создания аккаунта", auto_now_add=True)
    email = models.EmailField("Почта", unique=True)
    residents = models.IntegerField("Кол-во жильцов", default=3, validators=[validate_residents])
    is_active = models.BooleanField("active", default=False)
    username = None  # Удаляем поле 'username'
    first_name = models.CharField("Имя" , max_length=20, blank=True, validators=[validate_first_name])
    last_name = models.CharField("Фамилия", max_length=20, blank=True, validators=[validate_last_name])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['licSchet', 'residents']

    objects = UserManager()


    def __str__(self):
        return self.email

class Invoice(models.Model) :
    gasSumm = models.CharField("Сумма за газ", max_length=10, validators=[validate_gasSumm])
    waterSumm = models.CharField("Сумма за воду", max_length=10, validators=[validate_waterSumm])
    electroSumm = models.CharField("Сумма за энергию", max_length=10, validators=[validate_electroSumm])
    trashSumm = models.CharField("Сумма за мусор", max_length=10)
    repairSumm = models.CharField("Сумма за обслуживание дома", max_length=10)
    total = models.CharField("Общая сумма", max_length=10)
    date = models.DateTimeField("Дата создания квитанции", auto_now_add=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'invoice')

    def __str__(self):
        return f"Invoice for {self.date.year}.{self.date.month}.{self.date.day}"

class Data(models.Model) :
    gas = models.CharField("Показания газового счетчика", max_length=10)
    water = models.CharField("Показания водяного счетчика", max_length=10)
    electro = models.CharField("Показания счетчика энергии",  max_length=10)
    date = models.DateTimeField("Дата внесения показаний", auto_now_add=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE,  related_name = 'data', blank=True)
    costs = models.OneToOneField('Costs', on_delete=models.CASCADE, null=True,  related_name = 'data', blank=True)

    def __str__(self):
        return f"Meter for {self.date.year}.{self.date.month}.{self.date.day}"

class Costs(models.Model) :
    gasCost = models.CharField("Потребление газа", max_length=10)
    waterCost = models.CharField("Потребление воды", max_length=10)
    electroCost = models.CharField("Потребление энергии", max_length=10)
    date = models.DateTimeField("Дата внесения показаний", auto_now_add=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, unique=False,  related_name = 'costs')

    def __str__(self):
        return f"Costs for {self.date.year}.{self.date.month}.{self.date.day}"