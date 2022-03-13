from django.db import models


# Create your models here.


class Taomlar(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField()
    weight = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    is_added = models.BooleanField(default=False)



    class Meta:
        ordering = ["name"]
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

    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField()
    size = models.CharField(max_length=5, null=True, choices=SIZE, default='0.5L')
    price = models.IntegerField(default=0)
    is_added = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        # db_table = "ichimliklar"
