from django.urls import path
from .views import Home
from .api import urlpatterns as api_url

urlpatterns = [
    path('', Home.as_view(), name='home'),
]

urlpatterns += api_url
