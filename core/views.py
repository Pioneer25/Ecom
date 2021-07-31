from django.shortcuts import render
from product.models import Product
from customer.models import Customer
from vendor.models import Vendor
def base(request):
    customer_profile=Customer.objects.filter(created_by = request.user)
    vendor_profile=Vendor.objects.filter(created_by = request.user)

    return render(request,'core/base.html',{'customer_profile':customer_profile,'vendor_profile:':vendor_profile})  

# Create your views here.
def home(request):
    newest_products=Product.objects.all()[0:8]
    
    return render(request,'core/home.html',{'newest_products':newest_products})    
def contact(request):
    return render(request,'core/contact.html')