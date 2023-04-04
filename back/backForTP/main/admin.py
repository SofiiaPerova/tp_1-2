from django.contrib import admin

from main.models import *


# Register your models here.

class MeterInline(admin.StackedInline):
    model = Data


class InvoiceInline(admin.StackedInline):
    model = Invoice

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('licSchet', 'username', 'id')
    list_editable = ['username']
    list_filter = ('licSchet', 'username')
    search_fields = ['licSchet', 'username']
    readonly_fields = ['password']
    inlines = [InvoiceInline, MeterInline]

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('userID', 'date','gasSumm', 'waterSumm', 'electroSumm', 'trashSumm',
                    'repairSumm', 'total')
    list_editable = ('gasSumm', 'waterSumm', 'electroSumm', 'trashSumm',
                    'repairSumm', 'total')
    # list_filter = ('date')
    search_fields = ['userID']
    readonly_fields = ['date', 'userID']

@admin.register(Data)
class MeterAdmin(admin.ModelAdmin):
    list_display = ('userID', 'date','gas', 'water', 'electro')
    list_editable = ('gas', 'water', 'electro')
    # list_filter = ('date')
    search_fields = ['userID']
    readonly_fields = ['date', 'userID']


