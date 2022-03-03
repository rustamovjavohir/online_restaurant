from taomlar.models import (YaxnaTaomlar, QaynoqTaomlar,
                            BaliqliTaomlar, Ichimliklar,
                            Pizza, GoshtliTaomlar)
from taomlar.serializers import (TaomSerializer)
from .serializers import AdvertisingSerializer
from .models import Advertising


def some_data(model):
    data = model.objects.all()
    serializer = TaomSerializer(data=data, many=True)
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
    taom_list = [YaxnaTaomlar, QaynoqTaomlar, BaliqliTaomlar,
                 Pizza, GoshtliTaomlar, Ichimliklar]
    _.append({f"advertising": advertising_data()})
    for (model, _type) in zip(taom_list, taom_type):
        data = some_data(model)
        _.append({f"{_type}": data})
    return _