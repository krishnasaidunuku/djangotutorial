from django import forms
from .models import Employee,Project
class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput())

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'

