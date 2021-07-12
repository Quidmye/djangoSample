from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from computer.models import ComputerModel


class ComputerSerializer(ModelSerializer):

    brand = serializers.CharField(max_length=100)
    model = serializers.CharField(max_length=100)

    class Meta:
        model = ComputerModel
        fields = '__all__'

    def validate_memory(self, memory):
        if memory % 1024 != 0:
            raise serializers.ValidationError('Must be a multiple of 1024 ')
        return memory


