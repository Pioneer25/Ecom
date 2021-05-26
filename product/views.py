import random
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddToCartForm,CommentForm
from .models import  Product

from cart.cart import Cart


@login_required
def product(request, product_slug):
    cart = Cart(request)

    product = get_object_or_404(Product, slug=product_slug)
    comments = product.comments.filter(product=product)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'The product was added to the cart')

            return redirect('product', product_slug=product_slug)
    else:
        form = AddToCartForm()
    
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

           new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
           new_comment.product = product
            # Save the comment to the database
           new_comment.save()
            
            # Save the comment to the database
            
    else:
        comment_form = CommentForm()


    

    return render(request, 'product/product.html', {'form': form, 'product': product,'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, product.title + " has been removed from your WishList")
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, "Added " + product.title + " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "product/user_wish_list.html", {"wishlist": products})