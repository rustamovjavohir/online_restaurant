from django.urls import path
from .views import BuyurtmaView
from .api import urlpatterns as api_urls

urlpatterns = [
    path('buyurtma/', BuyurtmaView.as_view(), name='buyurtma_berish'),
]

urlpatterns += api_urls
