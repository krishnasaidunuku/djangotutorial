from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.CharField(max_length=50)
    ename=models.CharField(max_length=50)
    esalary=models.FloatField()
    emobile=models.IntegerField()
    def __str__(self):
        return self.ename




