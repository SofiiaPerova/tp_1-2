from djoser.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *

class UserCustomSerializer(serializers.ModelSerializer) :
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['id', 'licSchet', 'email', 'residents', 'username', 'is_active']

class AdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_staff')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            is_staff=True
        )
        return user

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


class UserDataSerializer(serializers.ModelSerializer) :
    data = dataSerializer(many=True)
    invoice = invoiceSerializer(many=True)
    costs = CostsSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'licSchet', 'email', 'residents', 'data', 'costs', 'invoice']





