from django.db import models
from django.contrib.auth.models import User


class Empdata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    emp_id=models.CharField(max_length=200)
    working=models.BooleanField(default=True)
    jdate=models.CharField(max_length=200)
    ldate=models.CharField(max_length=200)
    dept=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    add=models.CharField(max_length=1500)
    state=models.CharField(max_length=200)
    idproof=models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)






    
