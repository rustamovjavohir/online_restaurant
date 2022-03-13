from .views import AdvertisingViewSet
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()

routers.register(f'advertising', AdvertisingViewSet, basename='advertising')
urlpatterns = routers.urls
