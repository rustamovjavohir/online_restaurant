from django.shortcuts import render
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404

from auth_user.models import User
from auth_user.user_jwt import L_JWTAuthentication
from auth_user.utils import check_token
from buyurtmalar.models import Savatcha, Buyurtma
from buyurtmalar.serializers import SavatchaSerializer, BuyurtmaSerializer, BuyurtmaJadvalSerializer
from buyurtmalar.utils import savat_2_buyurtma, savatga_qoshish


class BasketView(ModelViewSet):
    queryset = Savatcha.objects.all()
    serializer_class = SavatchaSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticated]
    authentication_classes = [L_JWTAuthentication]

    def get_queryset(self):
        self.queryset = Savatcha.objects.filter(mijoz_id=self.request.user.id, is_deleted=False)
        return self.queryset

    @swagger_auto_schema(operation_summary="Savatchadagi mahsulotlarni chop etadi")
    def list(self, request, *args, **kwargs):
        return super(BasketView, self).list(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Savatdagi mahsulotlarni chop etish(retrive)")
    def retrieve(self, request, *args, **kwargs):
        return super(BasketView, self).retrieve(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Mahsulotni savatga qoshish")
    def create(self, request, *args, **kwargs):
        if Savatcha.objects.filter(mahsulot=request.data.get('mahsulot').upper(), mijoz=request.user.id).exists():
            return Response({"message": "you have already purchased this product"}, status=status.HTTP_200_OK)
        data = savatga_qoshish(request)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(operation_summary="Savatchadagi ma`lumotlarni qisaman o'zgartirish")
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Savatchadagi ma`lumotlarni o`zgartirish")
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
    @swagger_auto_schema(operation_summary="Savatchadagi mahsulotlarni ochirish")
    def destroy(self, request, *args, **kwargs):
        return super(BasketView, self).destroy(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Savatdagi mahsulot sonini oshirish")
    @action(methods=['post'], detail=False, url_path='add', url_name='add_item')
    def add(self, request, *args, **kwargs):
        mahsulot = Savatcha.objects.filter(mahsulot=str(request.data.get('mahsulot')).upper(),
                                           mijoz=request.user.id, is_deleted=False).first()
        mahsulot.count += 1
        mahsulot.save()
        return Response({"message": "successfully"}, status=status.HTTP_200_OK)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Savatdagi mahsulot sonini kamaytirish")
    @action(methods=['post'], detail=False, url_path='subtraction', url_name='subtraction_item')
    def subtraction(self, request, *args, **kwargs):
        mahsulot = Savatcha.objects.filter(mahsulot=str(request.data.get('mahsulot')).upper(),
                                           mijoz=request.user.id, is_deleted=False).first()
        if mahsulot.count > 0:
            mahsulot.count -= 1
        mahsulot.save()
        return Response({"message": "successfully"}, status=status.HTTP_200_OK)


class BuyurtmaView(GenericAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAuthenticated]
    authentication_classes = [L_JWTAuthentication]

    @transaction.atomic
    @swagger_auto_schema(operation_summary='Buyurtma yetkazib berishni rasmiylashtirish')
    def post(self, request, *args, **kwargs):
        """
        Buyurtma yetkazib berishni rasmiylashtirish
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        id = serializer.data.get('id')
        savat_2_buyurtma(b_id=id, user_id=request.user.id)
        # headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


