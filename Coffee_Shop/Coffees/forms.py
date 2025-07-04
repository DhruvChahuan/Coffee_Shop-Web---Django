from django import forms
from .models import Users,Order

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name','email','mobile_no','message']

class PlaceOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user','coffee','quantity']