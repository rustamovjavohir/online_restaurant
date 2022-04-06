from django.db import models
from .utils import taom_nomlari, taom_narxi
from taomlar.models import *
from auth_user.models import User
# Create your models here.


class Buyurtma(models.Model):

    DELIVERY_TYPE = (('YETKAZIB BERISH', 'Yetkazib berish'),
                     ('BORIB OLISH', 'Borib olish'))
    PAYMENT_TYPE = (('KARTA ORQALI', 'Karta orqali'),
                    ('NAQD PUL', 'Naqd pul'))

    DISTRICT = (("BEKTEMIR", "Bektemir"), ("MIROBOD", "Mirobod"), ("MIRZO ULUGBEK", "Mirzo Ulug'bek"),
                ("CHILONZOR", "Chilonzor"), ("OLMAZOR", "Olmazor"), ("SERGELI", "Sergeli"),
                ("SHAYHONTOHUR", "Shayhontohur"), ("UCHTEPA", "Uchtepa"), ("YAKKASAROY", "Yakkasaroy"),
                ("YASHNAOBOD", "Yashnaobod"), ("YUNUSOBOD", "Yunusobod"),)

    user_name = models.CharField(max_length=250, null=False, blank=False)
    phone = models.CharField(max_length=13, null=False, blank=False)
    delivery_type = models.CharField(max_length=50, choices=DELIVERY_TYPE, default="YETKAZIB BERISH")
    address = models.CharField(max_length=250, choices=DISTRICT, default="YUNUSOBOD")
    street = models.CharField(max_length=250, null=False, blank=False)
    flat = models.CharField(max_length=50, null=False, blank=False)
    descriptions = models.CharField(max_length=250)
    payment = models.CharField(max_length=100, choices=PAYMENT_TYPE, default='Naqd pul')
    call = models.BooleanField(default=False)
    product_list = models.CharField(max_length=10000, default=1)
    # pan = models.IntegerField(default=0)
    # expiry_date = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.address },{self.street},{self.flat} : {self.phone}"


class Savatcha(models.Model):
    mijoz = models.ForeignKey(User, on_delete=models.CASCADE)
    mahsulot = models.CharField(max_length=250, choices=taom_nomlari())
    count = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.mijoz.username} {self.mahsulot}"


class BuyurtmaJadval(models.Model):
    basket = models.ForeignKey(Savatcha, on_delete=models.CASCADE)
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.buyurtma.user_name}: {self.basket.mahsulot} date:{self.date}, done:{self.delivered}"

    class Meta:
        ordering = ['date']



