from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index.as_view(),name='index'),
    path('emp/',views.employee_details.as_view(),name='emp'),
    path('update/<int:id>',views.Employee_update.as_view(),name='update')

]