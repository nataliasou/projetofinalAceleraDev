from rest_framework import serializers
from .models import User


class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'active', 'staff', 'admin']


