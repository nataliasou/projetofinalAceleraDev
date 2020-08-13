from rest_framework import serializers
from .models import ErrorInstances


class ErrorInstancesModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ErrorInstances
        fields = ['id', 'level', 'events', 'type_error', 'title', 'shelved', 'user_id', 'description', 'origin', 'date', 'details']
