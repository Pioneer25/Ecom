from django.contrib import admin
from .models import Customer,Comment_product,my_balance

# Register your models here.
admin.site.register(Customer)
admin.site.register(Comment_product)
admin.site.register(my_balance)
