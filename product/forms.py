from django import forms
from customer.models import Comment_product

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_product
        fields = ('body',)

