from rest_framework import serializers
from main.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'licSchet', 'password', 'is_staff']