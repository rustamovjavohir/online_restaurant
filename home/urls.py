from django.urls import path
from .views import Home, Discount
from .api import urlpatterns as api_url

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('increase_price/', Discount.as_view(), name='increase_price'),
]

urlpatterns += api_url
