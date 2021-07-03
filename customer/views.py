from cart.models import OrderItem
from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Customer,my_balance
from django.utils.text import slugify
from product.models import Product
from .forms import balanceForm



# Create your views here.
def become_customer(request,backend='django.contrib.auth.backends.ModelBackend'):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user,backend='django.contrib.auth.backends.ModelBackend')

            customer = Customer.objects.create(name=user.username, created_by=user)

            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'customer/become_customer.html', {'form': form})

@login_required
def customer_admin(request):
    my_user_profile = Customer.objects.filter(name=request.user).first()
    my_orders=OrderItem.objects.filter(owner=my_user_profile)
    user = my_balance.objects.filter(user_balance=my_user_profile)
	 
	
    return render(request,'customer/customer_admin.html',{'my_user_profile':my_user_profile,'my_orders':my_orders,'user':user})
@login_required
def balance(request):
    form=balanceForm()
    if request.method == 'POST':
        form = balanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'customer/balance.html', {'form': form})
@login_required
def updatebalance(request,pk):
    customers=request.user.customer(id=pk)
    form=balanceForm(instance=customers)
    if request.method == 'POST':
        form = balanceForm(request.POST,instance=customers)

        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'customer/balance.html', {'form': form})

@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "customer/user_wish_list.html", {"wishlist": products})