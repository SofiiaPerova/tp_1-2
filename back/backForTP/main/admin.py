from django.contrib import admin
from django.contrib.auth.models import Group

from main.models import *


# Register your models here.

class MeterInline(admin.StackedInline):
    model = Data
    extra = 1
    verbose_name_plural = 'Показания счетчиков'
    classes = ['collapse']
    fields = ['gas', 'water',
              'electro', 'date']
    readonly_fields = ['date']
    verbose_name = 'Показания за '
    verbose_name_plural = 'Показания счетчиков'


class InvoiceInline(admin.StackedInline):
    model = Invoice
    extra = 1
    verbose_name_plural = 'Квитанции'
    classes = ['collapse']
    fields = ['gasSumm', 'waterSumm','electroSumm',
              'trashSumm', 'repairSumm', 'total','date']
    readonly_fields = ['date']
    verbose_name = 'Квитанция за '
    verbose_name_plural = 'Квитанции'

class CostsInLine(admin.StackedInline) :
    model = Costs
    extra = 1
    verbose_name_plural = 'Потребление услуг'
    classes = ['collapse']
    fields = ['gasCost', 'waterCost',
              'electroCost', 'date']
    readonly_fields = ['date']
    verbose_name = 'Потребление за '
    verbose_name_plural = 'Потребление услуг'
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'licSchet', 'id')
    list_filter = ('licSchet', 'email')
    search_fields = ['licSchet', 'email']
    exclude = ('password', 'first_name', 'last_name',
               'date', 'date_joined', 'last_login', 'group')
    inlines = [MeterInline, CostsInLine, InvoiceInline]


# @admin.register(Invoice)
# class InvoiceAdmin(admin.ModelAdmin):
#     list_display = ('userID', 'date','gasSumm', 'waterSumm', 'electroSumm', 'trashSumm',
#                     'repairSumm', 'total')
#     list_editable = ('gasSumm', 'waterSumm', 'electroSumm', 'trashSumm',
#                     'repairSumm', 'total')
#     # list_filter = ('date')
#     search_fields = ['userID']
#     readonly_fields = ['date', 'userID']
#
# @admin.register(Data)
# class MeterAdmin(admin.ModelAdmin):
#     list_display = ('userID', 'date','gas', 'water', 'electro')
#     list_editable = ('gas', 'water', 'electro')
#     # list_filter = ('date')
#     search_fields = ['userID']
#     readonly_fields = ['date', 'userID']


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'licSchet', 'residents', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'licSchet')


    fieldsets = (
        (None, {'fields': ('email', 'licSchet', 'residents')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'licSchet', 'password1', 'password2'),
        }),
    )

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
