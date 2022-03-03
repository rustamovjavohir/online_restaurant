from django.contrib import admin
from .models import (QaynoqTaomlar, SuyuqTaomlar, YaxnaTaomlar,
                    Pizza, GoshtliTaomlar, BaliqliTaomlar, Ichimliklar)


@admin.register(QaynoqTaomlar)
class QaynoqTaomlarAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(SuyuqTaomlar)
class SuyuqTaomlarAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(YaxnaTaomlar)
class YaxnaTaomlarAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(GoshtliTaomlar)
class GoshtliTaomlarAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(BaliqliTaomlar)
class BaliqliTaomlarAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Ichimliklar)
class IchimliklarAdmin(admin.ModelAdmin):
    list_display = ['name']



