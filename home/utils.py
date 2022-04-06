from datetime import datetime

import pytz

from taomlar.models import (YaxnaTaomlar, QaynoqTaomlar,
                            BaliqliTaomlar, Ichimliklar,
                            GoshtliTaomlar)
from taomlar.serializers import (YaxnaTaomlarSerializer, QaynoqTaomlarSerializer,
                                 BaliqliTaomlarSerializer, IchimliklarSerializer,
                                 GoshtliTaomlarSerializer)
from taomlar.utils import accessory_model
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
                 "goshtlitaomlar"]
    url_path = ["yaxnataom", "qaynoqtaom", "baliqlitaom",
                "goshtli"]
    taom_nomi = ["Yaxna taomlar", "Qaynoq Taomlar", "Baliqli Taomlar",
                 "Go'shtli Taomlat"]
    ser_class = [YaxnaTaomlarSerializer, QaynoqTaomlarSerializer,
                 BaliqliTaomlarSerializer,
                 GoshtliTaomlarSerializer]
    taom_list = [YaxnaTaomlar, QaynoqTaomlar, BaliqliTaomlar,
                 GoshtliTaomlar, ]
    _.append({"url": "advertising", "code": "advertising", "name": "Reklama", f"data": advertising_data()})
    for (url_p, nomi, model, _type, serializer) in zip(url_path, taom_nomi, taom_list, taom_type, ser_class):
        data = some_data(model, serializer_class=serializer)
        accessory_data = accessory_model(_type.upper())
        _.append(
            {"url": f"{url_p}", "code": f"{_type}", "name": f"{nomi}", "data": data, "accessory_data": accessory_data})
    return _


# def discount(queryset):
#     foods = queryset
#     dic_foods = Advertising.objects.filter(is_deleted=False)
#     for dic_food in dic_foods:
#         for food in foods:
#             if dic_food.food_id == food.id:
#                 food.price = dic_food.new_price
#     return foods


def advertising_date():
    advertising = Advertising.objects.filter(is_deleted=False)
    utc = pytz.UTC
    for adv in advertising:
        finish_date = adv.finish_date.replace(tzinfo=utc)
        now = datetime.now().replace(tzinfo=utc)
        if finish_date <= now:
            adv.is_deleted = True
            adv.save()
