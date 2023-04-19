import re

from rest_framework.exceptions import ValidationError


def validate_licSchet(value) :
    if not re.match('\d{2}[A-B]{2}\d{6}', value):
        raise ValidationError('Лицевой счет должен содержать 2 цифры + 2 заглавные латинские буквы + 6 цифр')

def validate_residents(value) :
    if not re.match('\d', value):
        raise ValidationError('Колличество жильцов варьируется 1-9')

def validate_first_name(value) :
    if not re.match('[А-Я][а-я]{1-15}', value):
        raise ValidationError('Имя состоит из букв русского алфавита и начинается с заглавной буквы')

def validate_last_name(value) :
    if not re.match('[А-Я][а-я]{1-15}', value):
        raise ValidationError('Фамилия состоит из букв русского алфавита и начинается с заглавной буквы')

def validate_gasSumm(value) :
    if not re.match('\d{1,6}', value):
        raise ValidationError('Показания газа должны содержать от 1 до 6 цифр')

def validate_waterSumm(value) :
    if not re.match('\d{1,6}', value):
        raise ValidationError('Показания воды должны содержать от 1 до 6 цифр')

def validate_electroSumm(value) :
    if not re.match('\d{1,6}', value):
        raise ValidationError('Показания энергии должны содержать от 1 до 6 цифр')