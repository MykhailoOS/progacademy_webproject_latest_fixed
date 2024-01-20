from django import forms
from furni.models import Checkout


class OrderForm(forms.ModelForm):
    """
    Form for Order model
    """
    class Meta:
        model = Checkout
        fields = ('first_name', 'last_name', 'country', 'company_name', 'address'
                  , 'postal_code', 'email', 'phone', 'message', 'is_approved')


class EditOrderForm(forms.ModelForm):
    """
    Form for editing
    """
    class Meta:
        model = Checkout
        fields = (
            'first_name', 'last_name', 'country', 'company_name', 'address', 'postal_code', 'email', 'phone', 'message',
            'is_approved')
