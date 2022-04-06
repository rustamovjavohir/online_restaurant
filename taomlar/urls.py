from django.urls import path
from .api import urlpatterns as api_urls
from .views import (YaxnaTaomlarList, QaynoqTaomlarList,
                    SuyuqTaomlarList, BaliqliTaomlarList,
                    PizzaList, GoshtliTaomlarList, IchimliklarList, AccessoryModelCode)

urlpatterns = [
    path("yaxnataomlist/", YaxnaTaomlarList.as_view(), name="yaxnataomlist"),
    path("qaynoqtaomlist/", QaynoqTaomlarList.as_view(), name="qaynoqtaomlist"),
    path("suyuqtaomlist/", SuyuqTaomlarList.as_view(), name="suyuqtaomlist"),
    path("baliqlitaomlist/", BaliqliTaomlarList.as_view(), name="baliqlitaomlist"),
    path("pizzalist/", PizzaList.as_view(), name="pizzalist"),
    path("goshtlitaomlist/", GoshtliTaomlarList.as_view(), name="goshtlitaomlist"),
    path("ichimliklist/", IchimliklarList.as_view(), name="ichimliklist"),
    path("modelcode/<str:model_code>/", AccessoryModelCode.as_view(), name="accessory")
]

urlpatterns += api_urls
