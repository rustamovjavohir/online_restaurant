from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from auth_user.user_jwt import L_JWTAuthentication
from taomlar.models import Pizza
from .models import Advertising
from .serializers import AdvertisingSerializer
from .utils import full_data, YaxnaTaomlar, advertising_date


class Home(GenericAPIView):
    queryset = Pizza.objects.all()
    serializer_class = YaxnaTaomlar
    lookup_field = ['name']
    filter_backends = (filters.SearchFilter,)
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(operation_summary="Home")
    def get(self, request, *args, **kwargs):
        advertising_date()
        data = full_data()
        return Response(data, status=status.HTTP_200_OK)


class AdvertisingViewSet(ModelViewSet):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
    parser_classes = (MultiPartParser, )
    # permission_classes = [IsAdminUser]
    # authentication_classes = [L_JWTAuthentication]

    @swagger_auto_schema(operation_summary="Reklamalar ro'yhatini chop etadi")
    def list(self, request, *args, **kwargs):
        queryset = Advertising.objects.filter(is_deleted=False)
        queryset = self.filter_queryset(queryset=queryset)
        advertising_date()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        # return super(AdvertisingViewSet, self).list(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Reklamalar ro'yhatini chop admin uchun (vaqti tugaganlarni ham chop etadi)")
    @action(methods=['get'], detail=False, url_path='list_advertising', url_name='list_advertising')
    def list_advertising(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary="Reklama haqidagi ma'lumotni chop etish(retrive)")
    def retrieve(self, request, *args, **kwargs):
        return super(AdvertisingViewSet, self).retrieve(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yangi reklama yaratish")
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(operation_summary="Rekalmani qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Reklamadagi ma'lumotlarni yangilash")
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Reklama ma'lumotlarini ochirish")
    def destroy(self, request, *args, **kwargs):
        return super(AdvertisingViewSet, self).destroy(self, request, *args, **kwargs)
