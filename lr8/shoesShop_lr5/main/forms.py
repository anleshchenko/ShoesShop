from django.core import validators
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Shoes, Manufacturer, Color, Category


class AddShoes(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ['SKU', 'name', 'price', 'size', 'category', 'color', 'manufacturer']
        widgets = {
            'SKU': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'manufacturer': forms.Select(attrs={'class': 'form-control'}),
        }


class AddManufacturer(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddColor(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
