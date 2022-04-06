from .views import BasketView, BuyurtmaView
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()


routers.register(f'basket', BasketView, basename='basket')
routers.register(f'buyurtma', BuyurtmaView, basename='buyurtma')

urlpatterns = routers.urls
