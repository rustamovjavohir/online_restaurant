from rest_framework.serializers import ModelSerializer
from .models import BuyurtmaJadval, Buyurtma, Savatcha


class BuyurtmaJadvalSerializer(ModelSerializer):
    class Meta:
        model = BuyurtmaJadval
        fields = '__all__'


class BuyurtmaSerializer(ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'


class SavatchaSerializer(ModelSerializer):
    class Meta:
        model = Savatcha
        fields = '__all__'
