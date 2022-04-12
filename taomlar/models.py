from django.db import models
import time
import uuid

# Create your models here.


class Taomlar(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.IntegerField(blank=True, unique=True, default=int(time.time() * 1000), primary_key=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    # weight = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    buy_count = models.IntegerField(default=1, blank=True,)
    is_added = models.BooleanField(default=False, blank=True,)



    class Meta:
        ordering = ["id"]
        abstract = True


class YaxnaTaomlar(Taomlar):

    def __str__(self):
        return self.name


class QaynoqTaomlar(Taomlar):

    def __str__(self):
        return self.name


class GoshtliTaomlar(Taomlar):

    def __str__(self):
        return self.name


class SuyuqTaomlar(Taomlar):

    def __str__(self):
        return self.name


class BaliqliTaomlar(Taomlar):

    def __str__(self):
        return self.name


class Pizza(Taomlar):
    SIZE_ = (("KATTA", "Katta"),
             ("STANDART", "Standart"),
             ("KICHIK", "Kichik"))
    TYPE_ = (("SIRLIK", "Sirlik"),
             ("QOZIQORINLIK", "Qo'ziqorinlik"),
             ("MARGORITA", "Margorita"))

    typepizza = models.CharField(max_length=50, choices=TYPE_, default="Sirlik")
    sizepizza = models.CharField(max_length=50, choices=SIZE_, default="Standart")

    def __str__(self):
        return self.typepizza


class Ichimliklar(models.Model):
    SIZE = (('0.5L', '0.5L'),
            ('1L', '1L'),
            ('1.5L', '1.5L'))

    id = models.IntegerField(default=int(time.time() * 1000), primary_key=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    size = models.CharField(max_length=5, null=True, choices=SIZE, default='0.5L')
    price = models.IntegerField(default=0)
    buy_count = models.IntegerField(default=1)
    is_added = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        # db_table = "ichimliklar"


class Accessory(models.Model):
    MODEL_CODE = (("YAXNATAOMLAR", "Yaxna Taomlar"),
                  ("GOSHTLITAOMLAR", "GoshtliTaomlar"),
                  ("QAYNOQTAOMLAR", "Qaynoqtaomlar"),
                  ("BALIQLITAOMLAR", "BaliqliTaomlar"))
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.IntegerField(blank=True, unique=True, default=int(time.time() * 1000), primary_key=True)
    model_code = models.CharField(choices=MODEL_CODE, max_length=250)
    name = models.CharField(max_length=250)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    price = models.IntegerField(default=0)
    buy_count = models.IntegerField(default=1, blank=True,)
    is_added = models.BooleanField(default=False, blank=True,)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
