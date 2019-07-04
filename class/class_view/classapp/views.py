from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Userregisterfrom
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method=='POST':
        forms=Userregisterfrom(request.POST)
        if forms.is_valid():
            forms.save()
            username=forms.cleaned_data.get('username')
            messages.success(request,f'Account is created for {username}')


    else:
            forms=Userregisterfrom()
    return render(request,'classapp/index.html',{'form':forms})


@login_required
def profile(request):
    return render(request,'classapp/profile.html')