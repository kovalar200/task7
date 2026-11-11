from django.shortcuts import render
from django.db import connection
from .models import (
    Заказы, Заказ_Продукция, Заказы_На_Производство_Продукция
)


def all_reports(request):

    orders = Заказы.objects.select_related('ЗаказчикУИД').all()

    order_products = Заказ_Продукция.objects.select_related(
        'Заказ_Покупателя_УИД__ЗаказчикУИД', 'Продукция_УИД'
    ).all()

    production = Заказы_На_Производство_Продукция.objects.select_related(
        'Продукция_УИД',
        'Заказ_Производства_УИД__Материал_УИД'
    ).all()

    context = {
        'orders': orders,
        'order_products': order_products,
        'production': production
    }
    return render(request, 'all_reports.html', context)