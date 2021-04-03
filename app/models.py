from django.db import models

class EmployeeModel(models.Model):
    idno=models.IntegerField(primary_key=True,unique=True)
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.FloatField()
    gender=models.CharField(max_length=10)
    contact=models.IntegerField()
    email=models.EmailField(default=None)
