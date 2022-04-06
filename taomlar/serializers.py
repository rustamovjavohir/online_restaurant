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
        # read_only_fields = ('id',)


class QaynoqTaomlarSerializer(ModelSerializer):
    class Meta:
        model = QaynoqTaomlar
        fields = '__all__'
        # read_only_fields = ('id',)


class SuyuqTaomlarSerializer(ModelSerializer):
    class Meta:
        model = SuyuqTaomlar
        fields = '__all__'
        # read_only_fields = ('id',)


class BaliqliTaomlarSerializer(ModelSerializer):
    class Meta:
        model = BaliqliTaomlar
        fields = '__all__'
        # read_only_fields = ('id',)


class GoshtliTaomlarSerializer(ModelSerializer):
    class Meta:
        model = GoshtliTaomlar
        fields = '__all__'
        read_only_fields = ('id',)


class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
        # read_only_fields = ('id',)


class IchimliklarSerializer(ModelSerializer):
    class Meta:
        model = Ichimliklar
        fields = '__all__'
        # read_only_fields = ('id',)


class AccessorySerializer(ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'
        # read_only_fields = ('id',)