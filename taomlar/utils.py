import random

from rest_framework.pagination import PageNumberPagination
from .models import Accessory
from .serializers import AccessorySerializer


class TaomPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000


def accessory_model(model_code):
    try:
        queryset = Accessory.objects.filter(model_code__icontains=model_code)
        serializer = AccessorySerializer(queryset, many=True)
        return serializer.data
    except Exception as e:
        return []


def unique_id():
    return random.randint(0, 9999999999)
