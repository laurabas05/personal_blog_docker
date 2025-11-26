from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            "class": "dark:bg-[#696969] mb-[10px] w-64 p-2 rounded-lg bg-[#d1d1d1] dark:text-white text-[#343434] focus:outline-none"
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "dark:bg-[#696969] mb-[10px] w-64 p-2 rounded-lg bg-[#d1d1d1] dark:text-white text-[#343434] focus:outline-none"
        })
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            "class": "dark:bg-[#696969] mb-[10px] w-64 p-2 rounded-lg bg-[#d1d1d1] dark:text-white text-[#343434] focus:outline-none"
        })
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "dark:bg-[#696969] mb-[10px] w-64 p-2 rounded-lg bg-[#d1d1d1] dark:text-white text-[#343434] focus:outline-none"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "dark:bg-[#696969] mb-[10px] w-64 p-2 rounded-lg bg-[#d1d1d1] dark:text-white text-[#343434] focus:outline-none"
    }))