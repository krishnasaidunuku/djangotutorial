from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.
class EmployeeCrud(ModelViewSet):
    queryset=Employee.objects.all()
    print(queryset,'udwuggqywg')
    serializer_class=EmployeeSerializer


