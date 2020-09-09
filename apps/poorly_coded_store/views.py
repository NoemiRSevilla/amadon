from django.shortcuts import render, redirect
from .models import Order, Product
from decimal import Decimal


def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method == "GET":
        totalorders = 0
        totalspent = 0
        for order in Order.objects.all():
            totalspent +=order.total_price
            totalorders += order.quantity_ordered
        context = {
            "previous": Order.objects.last(),
            "allorders": Order.objects.all(),
            "totalorders": totalorders,
            "totalspent": totalspent
        }
        return render(request, "store/checkout.html", context)

    if request.method == "POST":
        item = Order.objects.get(id=request.POST["product_id"])
        price_from_form = item.total_price
        quantity_from_form = item.quantity_ordered
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=price_from_form)
        return redirect ("/checkout")