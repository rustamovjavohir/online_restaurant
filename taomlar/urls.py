from django.urls import path
from .api import urlpatterns as api_urls

urlpatterns = []

urlpatterns += api_urls
