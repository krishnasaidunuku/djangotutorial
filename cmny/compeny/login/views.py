import hashlib
from django.shortcuts import render, redirect
from django.views import View
from django.template import loader
from django.http import HttpResponse

from .forms import UserAuthForm
from .models import Userauths


# Create your views here.

class RegisterView(View):

    def get(self, request):
        template = loader.get_template("loginapp/register.html")
        content = dict(
            login=UserAuthForm
        )
        return HttpResponse(template.render(content, request))

    def post(self, request):
        user = Userauths()
        user.email = request.POST["email"]
        passwrd = self.encrypt(request.POST["password"])
        user.password = passwrd
        user.save()
        return redirect("login")

    @staticmethod
    def encrypt(password):
        m = hashlib.sha256()
        m.update(password.encode())
        return m.digest()


class LoginView(View):

    def get(self, request):
        template = loader.get_template("loginapp/login.html")
        content = dict(
            login=UserAuthForm
        )
        return HttpResponse(template.render(content, request))

    def post(self, request):
        user = Userauths.objects.get(email=request.POST["email"])
        passwrd = self.encrypt(request.POST["password"])
        if user.password == passwrd:
            request.session["id"] = user.id
        template = loader.get_template("loginapp/register.html")
        content = dict(
            login=UserAuthForm
        )
        return HttpResponse(template.render(content, request))

    @staticmethod
    def encrypt(password):
        m = hashlib.sha256()
        m.update(password.encode())
        return m.digest()
