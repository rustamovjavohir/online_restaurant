from rest_framework import serializers


class AdvertisingSerializer(serializers.Serializer):
    descriptions = serializers.CharField(max_length=2500, allow_blank=True, allow_null=True)
    image = serializers.ImageField()
    start = serializers.DateTimeField()
    is_deleted = serializers.BooleanField(default=False)
