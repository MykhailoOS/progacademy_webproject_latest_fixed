from django import forms
from .models import Contact, Checkout
from django.core.validators import RegexValidator


class ContactForm(forms.ModelForm):
    """
    Contact form widgets
    """
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'fname'})
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'lname'})
    )
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'cols': '30', 'rows': '5'})
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')


class CheckoutForm(forms.ModelForm):
    """
    Checkout form widgets
    """
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'first_name'})
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'last_name'})
    )
    country = forms.CharField(
        label='Country',
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'country'})
    )
    company_name = forms.CharField(
        label='Company name',
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'company_name'})
    )
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'address'})
    )
    postal_code = forms.CharField(
        label='Postal code',
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'postal_code'})
    )
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'class': 'form-control custom-input', 'id': 'email'})
    )
    phone_regex = RegexValidator(regex=r'^\+?\d{7,12}$', message='Incorrect phone number')
    phone = forms.CharField(
        validators=[phone_regex, ],
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'id': 'phone'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'class': 'form-control custom-input', 'id': 'message', 'rows': '5'})
    )

    class Meta:
        model = Checkout
        fields = ('first_name', 'last_name', 'country', 'company_name', 'address',
                  'postal_code', 'email', 'phone', 'message')
