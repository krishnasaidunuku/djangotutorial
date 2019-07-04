from django import forms
from .models import Userauths


class UserAuthForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Userauths
        fields = ["email", "password"]