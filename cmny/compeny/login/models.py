from django.db import models

# Create your models here.

class Userauths(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 30)

class Userauthss(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 30)