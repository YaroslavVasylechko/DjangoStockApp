from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class FirmNames(forms.ModelForm):
    class Meta:
        model = FirmInfo
        fields = ['name', 'price', 'date']
        widgets = {
            'price': forms.TextInput(attrs={'class': 'form-control', }),
            'date': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'YYYY-mm-dd'}),
            'name': forms.Select(attrs={'class': 'form-control'}),
        }

    name = forms.ModelChoiceField(queryset=FirmName.objects.all(), empty_label='choose a firm name',
                                  to_field_name="name", widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))


class GetData(forms.ModelForm):
    class Meta:
        model = FirmInfo
        fields = ['name', ]
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
        }

    name = forms.ModelChoiceField(queryset=FirmName.objects.all(), empty_label='choose a firm name',
                                  to_field_name="name", widget=forms.Select(attrs={'class': 'form-select form-select-sm'}))

    from_date = forms.DateField(label='From date', widget=forms.DateInput(
        attrs={'class': 'form-control', 'placeholder': 'YYYY-mm-dd'}))
    to_date = forms.DateField(label='To date',
                              widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-mm-dd'}))
