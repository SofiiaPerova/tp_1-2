from djoser.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *

class UserCustomSerializer(serializers.ModelSerializer) :
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['id', 'licSchet', 'email', 'residents', 'username', 'is_active']

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'

class invoiceSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Invoice
        fields = '__all__'

class CostsSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Costs
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer) :
    data = dataSerializer(many=True)
    invoice = invoiceSerializer(many=True)
    costs = CostsSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'licSchet', 'email', 'residents', 'data', 'costs', 'invoice']





