from django.forms import ModelForm
from .models import my_balance

class balanceForm(ModelForm):
    class Meta:
        model = my_balance
        fields = ('balance','user_balance')