from .views import (YaxnaTaomlarViewset, PizzaViewset,
                    BaliqliTaomlarViewset, QaynoqTaomlarViewset,
                    SuyuqTaomlarViewset, GoshtliTaomlarViewset, IchimliklarViewset, AccessoryViewSet)
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()

routers.register(f'yaxnataom', YaxnaTaomlarViewset, basename='yaxnataomlar')
routers.register(f'qaynoqtaom', QaynoqTaomlarViewset, basename='qaynoqtaomlar')
# routers.register(f'suyuqtaom', SuyuqTaomlarViewset, basename='suyuqtaomlar')
routers.register(f'baliqlitaom', BaliqliTaomlarViewset, basename='baliqlitaomlar')
routers.register(f'goshtli', GoshtliTaomlarViewset, basename='goshtlitaomlar')
# routers.register(f'pizza', PizzaViewset, basename='pizza')
# routers.register(f'ichimliklar', IchimliklarViewset, basename='ichimliklar')
routers.register(f'accessory', AccessoryViewSet, basename='accessory')

urlpatterns = routers.urls
