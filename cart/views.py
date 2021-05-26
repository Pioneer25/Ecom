
from customer.models import Customer
from cart.models import Order ,OrderItem
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from customer.models import Customer
from .cart import Cart
from .forms import CheckoutForm
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def cart_detail(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
          

                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                zipcode = form.cleaned_data['zipcode']
                place = form.cleaned_data['place']

                order = checkout(request, first_name, last_name, email, address, zipcode, place, phone, cart.get_total_cost())

                cart.clear()
                notify_vendor(order)
                

                return redirect('success')
           
    else:
        form = CheckoutForm()

    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)

        return redirect('cart')
    
    if change_quantity:
        cart.add(change_quantity, quantity, True)

        return redirect('cart')

    return render(request, 'cart/cart.html', {'form': form})

def success(request):
    return render(request, 'cart/success.html')
def checkout(request, first_name, last_name, email, address, zipcode, place, phone, amount):
    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place, phone=phone, paid_amount=amount)
    user_profile = get_object_or_404(Customer,created_by=request.user)
    
    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'], vendor=item['product'].vendor,owner=user_profile, price=item['product'].price, quantity=item['quantity'])
    
        order.vendors.add(item['product'].vendor)
    return order
def notify_vendor(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    for vendor in order.vendors.all():
        to_email = vendor.created_by.email
        subject = 'New order'
        text_content = 'You have a new order!'
        html_content = render_to_string('cart/email_notify_vendor.html', {'order': order, 'vendor': vendor})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()