from django.contrib.auth.models import User
from .views import UserCreationForm
from django import forms
class Userregisterfrom(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']