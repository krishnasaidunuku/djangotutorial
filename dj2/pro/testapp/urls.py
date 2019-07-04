from django.conf.urls import url
from  django.urls import path
from . import views

urlpatterns = [
    path(r'app', views.emplist.as_view()),
    path(r'app/<int:pk>/', views.UserDetail.as_view(), name='UserDetail'),
]