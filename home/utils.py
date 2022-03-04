from taomlar.models import (YaxnaTaomlar, QaynoqTaomlar,
                            BaliqliTaomlar, Ichimliklar,
                            Pizza, GoshtliTaomlar)
from taomlar.serializers import (YaxnaTaomlarSerializer, QaynoqTaomlarSerializer,
                                 BaliqliTaomlarSerializer, IchimliklarSerializer,
                                 PizzaSerializer, GoshtliTaomlarSerializer)
from .models import Advertising
from .serializers import AdvertisingSerializer


def some_data(model, serializer_class):
    data = model.objects.all()
    serializer = serializer_class(data=data, many=True)
    serializer.is_valid()
    return serializer.data


def drink_data():
    data = Ichimliklar.objects.all()
    serializer = IchimliklarSerializer(data=data, many=True)
    serializer.is_valid()
    return serializer.data


def advertising_data():
    data = Advertising.objects.filter(is_deleted=False)
    serializer = AdvertisingSerializer(data=data, many=True)
    serializer.is_valid()
    return serializer.data


def full_data():
    _ = []
    taom_type = ["yaxnataomlar", "qaynoqtaomlar", "baliqlitaomlar",
                 "pizza", "goshtlitaomlar", "ichimliklar"]
    ser_class = [YaxnaTaomlarSerializer, QaynoqTaomlarSerializer,
                 BaliqliTaomlarSerializer, PizzaSerializer,
                 GoshtliTaomlarSerializer, IchimliklarSerializer]
    taom_list = [YaxnaTaomlar, QaynoqTaomlar, BaliqliTaomlar,
                 Pizza, GoshtliTaomlar, Ichimliklar]
    _.append({f"advertising": advertising_data()})
    for (model, _type, serializer) in zip(taom_list, taom_type, ser_class):
        data = some_data(model, serializer_class=serializer)
        _.append({f"{_type}": data})
    return _
