from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm
from .filters import OrderFilter

# Create your views here.
def home(request):
    customer = Customer.objects.all()
    order = Order.objects.all()
    total_customer = customer.count()
    total_order = order.count()
    pending = order.filter(status='Pending').count()
    delivered = order.filter(status='Delivered').count()
    dict = {
        'customers':customer, 'orders':order, 'total_customers':total_customer,
        'total_orders':total_order, 'pendings':pending, 'delivered':delivered
    }

    return render(request, 'accounts/dashboard.html', dict)

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})

def costumers(request, cust_id):
    customer = Customer.objects.get(id=cust_id)
    order = customer.order_set.all()
    total_order = order.count()

    myFilter = OrderFilter(request.GET, queryset=order)
    order = myFilter.qs

    dict = {
        'customers':customer, 'orders':order, 'total_orders':total_order, 'myFilter':myFilter
    }

    return render(request, 'accounts/costumers.html', dict)

def createOrder(request, cust_id):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=cust_id)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid:
            formset.save()
            return redirect("/")

    dict = {
        'formset':formset
    }

    return render(request, 'accounts/order_form.html', dict)

def updateOrder(request, cust_id):
    order = Order.objects.get(id=cust_id)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect("/")

    dict = { 'forms':form }

    return render(request, 'accounts/order_form.html', dict)

def deleteOrder(request, cust_id):
    order = Order.objects.get(id=cust_id)
    
    if request.method == 'POST':
        order.delete()
        return redirect("/")

    dict = { 'item':order }

    return render(request, 'accounts/ask_delete.html', dict)
