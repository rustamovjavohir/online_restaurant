from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, filters
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from taomlar.models import Pizza
from .utils import full_data, TaomSerializer


class Home(GenericAPIView):
    queryset = Pizza.objects.all()
    serializer_class = TaomSerializer
    lookup_field = ['name']
    filter_backends = (filters.SearchFilter,)
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(operation_summary="Home")
    def get(self, request, *args, **kwargs):
        data = full_data()
        return Response(data, status=status.HTTP_200_OK)


class Advertising(ModelViewSet):
    pass