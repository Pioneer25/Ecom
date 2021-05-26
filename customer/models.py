from django.contrib.auth.models import User
from django.db import models
from product.models import Product


class Customer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
class Comment_product(models.Model):
    user_product = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user_product)
class my_balance(models.Model):
    user_balance=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return str(self.user_balance)