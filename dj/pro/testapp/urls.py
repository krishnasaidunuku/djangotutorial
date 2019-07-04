from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'app', views.emplist.as_view()),
    url(r'user', views.userDetails.as_view()),
]