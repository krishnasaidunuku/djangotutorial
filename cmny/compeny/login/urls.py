from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register"),
    path("", views.LoginView.as_view(), name="login"),
]