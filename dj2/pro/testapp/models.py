from django.db import models
import uuid


class Employee(models.Model):

    # unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    def __str__(self):
        return self.firstname




