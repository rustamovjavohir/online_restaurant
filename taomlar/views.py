from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from auth_user.user_jwt import L_JWTAuthentication
from .models import *
from .serializers import *
from .utils import TaomPagination

"""
    Faqat adminlar uchun ochiq 
"""


class YaxnaTaomlarViewset(ModelViewSet):
    queryset = YaxnaTaomlar.objects.all()
    serializer_class = YaxnaTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser]
    authentication_classes = [L_JWTAuthentication]
    pagination_class = TaomPagination

    @swagger_auto_schema(operation_summary='Yaxnataomlar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(YaxnaTaomlarViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yangi yaxnataom kirish")
    def create(self, request, *args, **kwargs):
        return super(YaxnaTaomlarViewset, self).create(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yaxnataom malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        return super(YaxnaTaomlarViewset, self).update(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yaxnataom malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        return super(YaxnaTaomlarViewset, self).partial_update(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Yaxnataom malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(YaxnaTaomlarViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Yaxnataom haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(YaxnaTaomlarViewset, self).retrieve(self, request, *args, **kwargs)


class QaynoqTaomlarViewset(ModelViewSet):
    queryset = QaynoqTaomlar.objects.all()
    serializer_class = QaynoqTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser]
    authentication_classes = [L_JWTAuthentication]
    pagination_class = TaomPagination

    @swagger_auto_schema(operation_summary='Qaynoqtaomlar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(QaynoqTaomlarViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yangi qaynoqtaom kirish")
    def create(self, request, *args, **kwargs):
        return super(QaynoqTaomlarViewset, self).create(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Qaynoqtaom malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        return super(QaynoqTaomlarViewset, self).update(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Qaynoqtaom malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        return super(QaynoqTaomlarViewset, self).partial_update(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Qaynoqtaom malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(QaynoqTaomlarViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Qaynoqtaom haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(QaynoqTaomlarViewset, self).retrieve(self, request, *args, **kwargs)


class SuyuqTaomlarViewset(ModelViewSet):
    queryset = SuyuqTaomlar.objects.all()
    serializer_class = SuyuqTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser]
    authentication_classes = [L_JWTAuthentication]
    pagination_class = TaomPagination

    @swagger_auto_schema(operation_summary='Suyuqtaomlar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(SuyuqTaomlarViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yangi suyuqtaom kirish")
    def create(self, request, *args, **kwargs):
        return super(SuyuqTaomlarViewset, self).create(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Suyuqtaom malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        return super(SuyuqTaomlarViewset, self).update(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Suyuqtaom malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        return super(SuyuqTaomlarViewset, self).partial_update(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Suyuqtaom malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(SuyuqTaomlarViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Suyuqtaom haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(SuyuqTaomlarViewset, self).retrieve(self, request, *args, **kwargs)


class GoshtliTaomlarViewset(ModelViewSet):
    queryset = GoshtliTaomlar.objects.all()
    serializer_class = GoshtliTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    authentication_classes = [L_JWTAuthentication]
    permission_classes = [IsAdminUser]
    pagination_class = TaomPagination

    @swagger_auto_schema(operation_summary='Goshtlitaomlar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(GoshtliTaomlarViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yangi goshtlitaom kirish")
    def create(self, request, *args, **kwargs):
        return super(GoshtliTaomlarViewset, self).create(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Goshtlitaom malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        return super(GoshtliTaomlarViewset, self).update(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Goshtlitaom malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        return super(GoshtliTaomlarViewset, self).partial_update(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Goshtlitaom malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(GoshtliTaomlarViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Goshtlitaom haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(GoshtliTaomlarViewset, self).retrieve(self, request, *args, **kwargs)


class BaliqliTaomlarViewset(ModelViewSet):
    queryset = BaliqliTaomlar.objects.all()
    serializer_class = BaliqliTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser]
    authentication_classes = [L_JWTAuthentication]
    pagination_class = TaomPagination
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(operation_summary='Baliqlitaomlar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(BaliqliTaomlarViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yangi baliqlitaom kirish")
    def create(self, request, *args, **kwargs):
        return super(BaliqliTaomlarViewset, self).create(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Baliqlitaom malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        return super(BaliqliTaomlarViewset, self).update(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Baliqlitaom malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        return super(BaliqliTaomlarViewset, self).partial_update(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Baliqlitaom malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(BaliqliTaomlarViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Baliqlitaom haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(BaliqliTaomlarViewset, self).retrieve(self, request, *args, **kwargs)


class PizzaViewset(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = (filters.SearchFilter,)
    parser_classes = (MultiPartParser,)
    permission_classes = [IsAdminUser]
    authentication_classes = [L_JWTAuthentication]
    pagination_class = TaomPagination

    @swagger_auto_schema(operation_summary='Pitsalar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(PizzaViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yangi pitsa kirish")
    def create(self, request, *args, **kwargs):
        return super(PizzaViewset, self).create(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Pitsa malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        return super(PizzaViewset, self).update(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Pitsa malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        return super(PizzaViewset, self).partial_update(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Pitsa malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(PizzaViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Pitsa haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(PizzaViewset, self).retrieve(self, request, *args, **kwargs)


class IchimliklarViewset(ModelViewSet):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAdminUser]
    authentication_classes = [L_JWTAuthentication]
    parser_classes = (MultiPartParser,)
    pagination_class = TaomPagination

    @swagger_auto_schema(operation_summary='Ichimliklar royhatini chop etish')
    def list(self, request, *args, **kwargs):
        return super(IchimliklarViewset, self).list(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Yangi ichimlik kirish")
    def create(self, request, *args, **kwargs):
        return super(IchimliklarViewset, self).create(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Ichimlik malumotlarini yangilash")
    def update(self, request, *args, **kwargs):
        return super(IchimliklarViewset, self).update(self, request, *args, **kwargs)

    @transaction.atomic
    @swagger_auto_schema(operation_summary="Ichimlik malumotlarini qisman yangilash")
    def partial_update(self, request, *args, **kwargs):
        return super(IchimliklarViewset, self).partial_update(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Ichimlik malumotlarini o'chirish")
    def destroy(self, request, *args, **kwargs):
        return super(IchimliklarViewset, self).destroy(self, request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Ichimlik haqidagi malumotlarini chop etish (retrieve)")
    def retrieve(self, request, *args, **kwargs):
        return super(IchimliklarViewset, self).retrieve(self, request, *args, **kwargs)


"""
    Har qanday foydalanuvchi uchun ochiq
"""


class YaxnaTaomlarList(ListAPIView):
    queryset = YaxnaTaomlar.objects.all()
    serializer_class = YaxnaTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [AllowAny]
    lookup_field = ['name']
    parser_classes = (MultiPartParser,)
    pagination_class = TaomPagination


class QaynoqTaomlarList(ListAPIView):
    queryset = QaynoqTaomlar.objects.all()
    serializer_class = QaynoqTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [AllowAny]
    lookup_field = ['name']
    parser_classes = (MultiPartParser,)
    pagination_class = TaomPagination


class SuyuqTaomlarList(ListAPIView):
    queryset = SuyuqTaomlar.objects.all()
    serializer_class = SuyuqTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [AllowAny]
    lookup_field = ['name']
    parser_classes = (MultiPartParser,)
    pagination_class = TaomPagination


class GoshtliTaomlarList(ListAPIView):
    queryset = GoshtliTaomlar.objects.all()
    serializer_class = GoshtliTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [AllowAny]
    lookup_field = ['name']
    parser_classes = (MultiPartParser,)
    pagination_class = TaomPagination


class BaliqliTaomlarList(ListAPIView):
    queryset = BaliqliTaomlar.objects.all()
    serializer_class = BaliqliTaomlarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [AllowAny]
    lookup_field = ['name']
    parser_classes = (MultiPartParser,)
    pagination_class = TaomPagination


class PizzaList(ListAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [AllowAny]
    lookup_field = ['name']
    parser_classes = (MultiPartParser,)
    pagination_class = TaomPagination


class IchimliklarList(ListAPIView):
    queryset = Ichimliklar.objects.all()
    serializer_class = IchimliklarSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [AllowAny]
    lookup_field = ['name']
    parser_classes = (MultiPartParser,)
    pagination_class = TaomPagination
