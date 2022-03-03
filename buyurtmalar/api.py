from .views import BasketView
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()


routers.register(f'basket', BasketView, basename='basket')

urlpatterns = routers.urls
