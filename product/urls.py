from django.urls import path

from . import views

urlpatterns = [
    
    path('<slug:product_slug>/', views.product, name='product'),
   
    path("wishlist/add_to_wishlist/<int:id>", views.add_to_wishlist, name="user_wishlist"),
   
]
   
