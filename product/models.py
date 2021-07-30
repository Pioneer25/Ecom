from io import BytesIO
from PIL import Image
from django.contrib.auth.models import User

from django.core.files import File
from django.db import models

from vendor.models import Vendor



class Product(models.Model):
    
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=255)
    
    price = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=False, null=False)
    users_wishlist = models.ManyToManyField(User, related_name="user_wishlist", blank=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.title
    
    
   