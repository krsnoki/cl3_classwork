from django.contrib import auth
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import CustomerForm, OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import allowed_users, authenticated_user, admin_only

# Create your views here.
@authenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user=user,)
            messages.success(request, 'Account created successfully for ' + username)
            return redirect('login')

    dict = {'form': form}
    return render(request, 'accounts/register.html', dict)

@authenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username of password is incorrect!')

    dict = {}
    return render(request, 'accounts/login.html', dict)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
@admin_only
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

@login_required(login_url="login")
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    
    total_order = orders.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()

    dict = {'orders':orders, 'total_orders':total_order, 'pendings':pending, 'delivered':delivered}
    return render(request, 'accounts/user.html', dict)

@login_required(login_url="login")
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    dict = {'form':form}
    return render(request, 'accounts/account_settings.html', dict)

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url="login")
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, cust_id):
    order = Order.objects.get(id=cust_id)
    
    if request.method == 'POST':
        order.delete()
        return redirect("/")

    dict = { 'item':order }

    return render(request, 'accounts/ask_delete.html', dict)
