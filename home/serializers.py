from rest_framework import serializers
from .models import Advertising


class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertising
        fields = '__all__'
