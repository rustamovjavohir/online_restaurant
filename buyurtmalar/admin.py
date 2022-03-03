from django.contrib import admin
from .models import Buyurtma, BuyurtmaJadval, Savatcha


admin.site.register(Buyurtma)
admin.site.register(Savatcha)


@admin.register(BuyurtmaJadval)
class BuyurtmaJadvalAdmin(admin.ModelAdmin):
    list_filter = ['date']


