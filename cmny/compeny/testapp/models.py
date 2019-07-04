from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):

        return str(self.id)+self.name

    desc=models.TextField()
class Employee(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    age=models.IntegerField()
    mobile=models.IntegerField(default=0)
    projcet=models.ForeignKey(Project,on_delete=models.CASCADE)


    def __str__(self):

        return str(self.id)+self.firstname


