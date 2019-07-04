from django.shortcuts import render
from .models import Employee
from django.views import View
from django.http import HttpResponse
# Create your views here.
class list_get(View):
    def get(self,request):
        queryset=Employee.objects.all()
        return HttpResponse(queryset)