from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('become_customer/', views.become_customer, name='become_customer'),
    path('customer_admin/', views.customer_admin, name='customer_admin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='customer/login.html'), name='login'),
    path('updatebalance/<str:pk>/', views.updatebalance, name='updatebalance'),
    path("wishlist", views.wishlist, name="wishlist"),
    
   
    
   
]