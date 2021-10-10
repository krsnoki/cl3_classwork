from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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
    dict = {
        'customers':customer, 'orders':order, 'total_orders':total_order
    }
    return render(request, 'accounts/costumers.html', dict)
