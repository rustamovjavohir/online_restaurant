from taomlar.models import *
from collections import namedtuple


qay_taom = QaynoqTaomlar.objects.all()
yax_taom = YaxnaTaomlar.objects.all()
suy_taom = SuyuqTaomlar.objects.all()
gosht_taom = GoshtliTaomlar.objects.all()
pizza = Pizza.objects.all()
baliq_taom = BaliqliTaomlar.objects.all()
ichimlik = Ichimliklar.objects.all()


def taom_nomlari():
    taom_list = [qay_taom, yax_taom, suy_taom,
                 gosht_taom, pizza, baliq_taom, ichimlik]
    TAOM_NOMI = ()
    for obj_list in taom_list:
        for obj in obj_list:
            my_tuple = ((f"{obj.name.upper()}", f"{obj.name}"),)
            TAOM_NOMI += my_tuple
    return TAOM_NOMI


def taom_narxi():
    taom_list = [qay_taom, yax_taom, suy_taom,
                 gosht_taom, pizza, baliq_taom, ichimlik]
    NARXI = ()
    for obj_list in taom_list:
        for obj in obj_list:
            my_tuple = ((f"{obj.price}", f"{obj.price}"),)
            NARXI += my_tuple
    return NARXI


def savat_2_buyurtma(b_id, user_id):
    from .models import Savatcha, BuyurtmaJadval
    savat = Savatcha.objects.filter(mijoz_id=user_id, is_deleted=False)
    for i in savat:
        i.is_deleted = True
        BuyurtmaJadval(basket=i, buyurtma_id=b_id).save()
        i.save()


def savatga_qoshish(request):
    data = {
        "mahsulot": request.data.get('mahsulot'),
        "mijoz": request.user.id,
        "count": request.data.get('count'),
        "is_deleted": request.data.get('is_deleted')
    }

    return data



