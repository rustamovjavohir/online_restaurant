from django.urls import path
from .api import urlpatterns as api_urls

urlpatterns = [
    # path('buyurtma/', BuyurtmaView.as_view(), name='buyurtma_berish'),
    # path('buyurtma/<int:pk>/', BuyurtmaDestroyView.as_view(), name='buyurtmani ochirish'),
]

urlpatterns += api_urls
