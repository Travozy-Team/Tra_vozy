# forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'package_id', 'package_type', 'package_title', 'package_price',
            'full_name', 'email', 'phone', 'travel_date', 
            'number_of_travelers', 'special_requests'
        ]
        
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'fullName',
                'required': True,
                'autocomplete': 'off'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'required': True,
                'autocomplete': 'off',
                'style': 'text-transform: lowercase;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'required': True,
                'autocomplete': 'off'
            }),
            'travel_date': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'travelDate',
                'type': 'date',
                'required': True
            }),
            'number_of_travelers': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'travelers',
                'min': '1',
                'value': '1',
                'required': True
            }),
            'special_requests': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'specialRequests',
                'rows': '4'
            }),
            'package_id': forms.HiddenInput(attrs={'id': 'packageId'}),
            'package_type': forms.HiddenInput(),
            'package_title': forms.HiddenInput(),
            'package_price': forms.HiddenInput(),
        }