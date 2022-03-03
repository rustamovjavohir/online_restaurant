from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import *


class TaomSerializer(Serializer):
    name = serializers.CharField(max_length=250)
    description = serializers.CharField(max_length=5000000)
    image = serializers.ImageField()
    weight = serializers.IntegerField(default=0)
    price = serializers.FloatField(default=0)


class YaxnaTaomlarSerializer(ModelSerializer):
    class Meta:
        model = YaxnaTaomlar
        fields = '__all__'


class QaynoqTaomlarSerializer(ModelSerializer):
    class Meta:
        model = QaynoqTaomlar
        fields = '__all__'


class SuyuqTaomlarSerializer(ModelSerializer):
    class Meta:
        model = SuyuqTaomlar
        fields = '__all__'


class BaliqliTaomlarSerializer(ModelSerializer):
    class Meta:
        model = BaliqliTaomlar
        fields = '__all__'


class GoshtliTaomlarSerializer(ModelSerializer):
    class Meta:
        model = GoshtliTaomlar
        fields = '__all__'


class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class IchimliklarSerializer(ModelSerializer):
    class Meta:
        model = Ichimliklar
        fields = '__all__'