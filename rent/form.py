from django import forms
from rent.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddPostForm(forms.ModelForm):
    class Meta:
        model = HouseDetail
        fields = ['user', 'contact_person', 'location', 'mobile', 'rent_type', 'room_number', 'client_type_a', 'client_type', 'more_details', 'monthly_price', 'image']


class SearchRentForm(forms.Form):
    search_location = forms.CharField(max_length=222)
    search_rent_type = forms.CharField(max_length=222)
