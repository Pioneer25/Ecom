from django.forms import ModelForm

from product.models import Product
from django.utils.text import slugify

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [ 'image', 'title', 'description', 'price']