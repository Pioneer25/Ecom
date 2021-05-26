from django.http.response import HttpResponse
from cart.models import OrderItem
from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Vendor
from product.models import Product
from .forms import ProductForm
from django.utils.text import slugify
import xlwt
import datetime



# Create your views here.
def become_vendor(request,backend='django.contrib.auth.backends.ModelBackend'):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user,backend='django.contrib.auth.backends.ModelBackend')

            vendor = Vendor.objects.create(name=user.username, created_by=user)

            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'vendor/become_vendor.html', {'form': form})

@login_required
def vendor_admin(request):
    vendor = request.user.vendor 
    products=vendor.products.all()
    vendor_order=OrderItem.objects.filter(vendor=vendor)

    
    
    return render(request,'vendor/become_admin.html',{'vendor':vendor,'products':products,'vendor_order':vendor_order})
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm()
    
    return render(request, 'vendor/add_product.html', {'form': form})
def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['content-Disposition']='attachment;filename=orders'+\
        str(datetime.datetime.now())+'.xls'
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('orders')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True
    columns=['product','quantity','price']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)
    font_style=xlwt.XFStyle()
    rows=OrderItem.objects.filter(vendor=request.user.vendor).values_list('product','quantity','price')
    for row in rows:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)

    return response

