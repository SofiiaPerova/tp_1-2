from djoser.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *

class UserCustomSerializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = "__all__"

class dataSerializer(serializers.ModelSerializer):
    userID = serializers.StringRelatedField()

    class Meta:
        model = Data
        fields = '__all__'

class invoiceSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Invoice
        fields = '__all__'



